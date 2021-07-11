#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Connect to the given node wallets address and collect small outputs into one bigger output to the same address. Works
only with node wallet address. Node wallet must be unlocked already. This script leave the boxes with assets (tokens)
untouched and collect only the simple boxes with ERGs only. Script does not take into account current mempool
transactions. Multiple node wallet addresses not supported.

Requirements: pure Python 3.6.9+
"""
import argparse
import json
import urllib.request as ur


def callapi(uri: str, data=None):
    """Make GET (data=None) or POST (data!=None) requests to given node API"""
    if data is not None:
        data = json.dumps(data).encode('utf8')
    req = ur.Request(node_url + uri, data=data, headers=headers)
    res = ur.urlopen(req)
    jsonstr = res.read().decode('utf8')
    return json.loads(jsonstr)


def fmtbalance(balance):
    return '{} ERG ({} nERG)'.format(balance/nanoerg, balance)


def fmtboxescount(cnt):
    return 'Boxes count: {}'.format(cnt)


if __name__ == '__main__':
    # Define and parse script arguments
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--node', metavar='127.0.0.1:9053', default='127.0.0.1:9053',
                        help='Ergo node API address (default is 127.0.0.1:9053)')
    parser.add_argument('--dust', metavar='100', default=100, type=int, help='Dust boxes count to collect '
                                                                             '(default is 100)')
    parser.add_argument('--fee', metavar='1000000', default=1_000_000, type=int, help='Fee, nERG (default is 1000000)')
    parser.add_argument('--send', action='store_true', help='If set, send transaction after signing it, otherwise just '
                                                            'print signed transaction without sending')
    parser.add_argument('--apikey', required=True, metavar='YOUR_API_KEY', help='Ergo node API key')
    parser.add_argument('--address', required=True, metavar='3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt',
                        help='Ergo node wallet address to look for dust output boxes')
    args = parser.parse_args()

    # Define global variables and constants
    headers = {'accept': 'application/json',
        'api_key': args.apikey,
        'Content-Type': 'application/json'
    }
    node_url = 'http://' + args.node
    address = args.address
    nanoerg = 1_000_000_000
    fee = args.fee
    dust_boxes_count = args.dust
    fee_ergo_tree = '1005040004000e36100204a00b08cd0279be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798ea02d192a39a8cc7a701730073011001020402d19683030193a38cc7b2a57300000193c2b2a57301007473027303830108cdeeac93b1a57304'

    # Retrieve all wallet unspent boxes
    data = callapi('/wallet/boxes/unspent')
    boxes = {}
    distribution = {}
    for box in data:
        value = box['box']['value']
        box_id = box['box']['boxId']
        if box['onchain']:
            addr = box['address']
            if addr not in boxes:
                boxes[addr] = {
                    'without_assets': {'count': 0, 'balance': 0, 'ids': {}},
                    'with_assets': {'count': 0, 'balance': 0, 'ids': {}}
                }
            assets = 'with_assets' if box['box']['assets'] else 'without_assets'
            boxes[addr][assets]['count'] += 1
            boxes[addr][assets]['balance'] += value
            if value not in boxes[addr][assets]['ids']:
                boxes[addr][assets]['ids'][value] = []
            boxes[addr][assets]['ids'][value].append(box_id)

            if addr == address and not box['box']['assets']:
                if value not in distribution:
                    distribution[value] = 1
                else:
                    distribution[value] += 1

    values = sorted(distribution.keys())
    inputsRaw = []
    balance = 0
    for value in values:
        for box_id in boxes[address]['without_assets']['ids'][value]:
            inputsRaw.append(box_id)
            balance += value
            if len(inputsRaw) == dust_boxes_count:
                break
        if len(inputsRaw) == dust_boxes_count:
            break

    # Show common wallet addresses info
    print()
    print('Wallet addresses information:')
    for addr in boxes:
        print()
        print('==={}==='.format(addr))
        for assets in ['without_assets', 'with_assets']:
            print('{}:'.format(assets.replace('_', ' ').capitalize()))
            print('  {}'.format(fmtboxescount(boxes[addr][assets]['count'])))
            print('  Balance: {}'.format(fmtbalance(boxes[addr][assets]['balance'])))
    print()
    print('===Boxes distribution for {} (without assets) ==='.format(address))
    for k in values:
        print('{: >15d}: {: >4d} ({})'.format(k, distribution[k], fmtbalance(k*distribution[k])))
    if boxes[address]['without_assets']['count'] < dust_boxes_count:
        print()
        print('There is no enough dust boxes to collect! You want to collect {} boxes, but there is {} dust boxes '
              '(and {} boxes without assets in total) for the given address {}'
              .format(dust_boxes_count, boxes[address]['without_assets']['count'] - 1,
                      boxes[address]['without_assets']['count'], address))
        exit(0)

    # Upcoming transaction info
    print()
    print('Upcoming transaction info:')
    print('Boxes to tx balance, nERG:', balance)
    print('Boxes to tx count:', len(inputsRaw))
    bigboxid = -2 if len(values) > 1 else 0
    print('Big Box Id: ', boxes[address]['without_assets']['ids'][values[bigboxid]][0])
    print('Big Box value: ', values[bigboxid])
    inputsRaw.append(boxes[address]['without_assets']['ids'][values[bigboxid]][0])
    balance += values[bigboxid] if len(values) > 1 else 0
    print('Total tx inputs value, nERG:', balance)
    print()

    # Generate request for /wallet/transaction/generate
    data = {
        "requests": [{
            "address": address,
            "value": balance - fee
        }],
        "fee": fee
    }
    # Get tx prototype from /wallet/transaction/generateUnsigned
    print('Get transaction prototype from {}/wallet/transaction/generateUnsigned...'.format(node_url), end='')
    txproto = callapi('/wallet/transaction/generateUnsigned', data)
    print('done.')

    # Search for creationHight, ergoTree from tx prototype
    ergo_tree = ''
    creation_height = 0
    for output in txproto['outputs']:
        if output['ergoTree'] != fee_ergo_tree:
            if ergo_tree:
                if output['ergoTree'] != ergo_tree:
                    print('Different ergo trees from transaction prototype outputs, multiple node wallet addresses not '
                          'supported, exiting!')
                    print('First found ergo tree: {}'.format(ergo_tree))
                    print('Second found ergo tree: {}'.format(output['ergoTree']))
                    exit(1)
            else:
                ergo_tree = output['ergoTree']
                creation_height = output['creationHeight']
    print('From transaction prototype extracted:')
    print('creationHight: {}'.format(creation_height))
    print('ergoTree: {}'.format(ergo_tree))
    print()

    # Generate unsigned tx for collecting dust boxes
    data = {
        'id': '',
        'inputs': [{'boxId': _, 'extension': {}} for _ in inputsRaw],
        'dataInputs': [],
        'outputs': [
            {
                'ergoTree': fee_ergo_tree, 'value': fee, 'additionalRegisters': {}, 'assets': [],
                'creationHeight': creation_height
            },
            {
                'ergoTree': ergo_tree, 'value': balance-fee, 'additionalRegisters': {}, 'assets': [],
                'creationHeight': creation_height
            }
        ]
    }
    print()

    # Signing transaction
    print('Signing transaction by sending it to {}/wallet/transaction/sign...'.format(node_url), end='')
    tx = callapi('/wallet/transaction/sign', {'tx': data})
    print('done!')
    print('Transaction id: {}'.format(tx['id']))
    print('Transaction size, bytes: {}'.format(tx['size']))
    print('Cost for byte, nERG: {:.0f}'.format(fee/tx['size']))
    print()

    # Send or print tx
    if args.send:
        print('Sending transaction via {}/transactions...'.format(node_url), end='')
        tx_id = callapi('/transactions', tx)
        print('done.')
        print('Sended transaction id: {}'.format(tx_id))
    else:
        print(json.dumps(tx, indent=4, sort_keys=True))
