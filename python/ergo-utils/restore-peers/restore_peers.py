#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Load a list of peers and add them to Ergo node (help to bootstrap node more quickly)"""
import argparse
import json
import time
import urllib.request as ur

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--file', metavar='peers.json', default='peers.json', help='JSON-file with peer list')
    parser.add_argument('--address', metavar='127.0.0.1:9053', default='127.0.0.1:9053', help='Ergo node API address')
    parser.add_argument('--apikey', required=True, metavar='YOUR_API_KEY', help='Ergo node API key')
    args = parser.parse_args()

    with open(args.file) as f:
        headers = {'accept': 'application/json',
                   'api_key': args.apikey,
                   'content-Type': 'application/json'
                   }
        url = 'http://' + args.address + '/peers/connect'
        peers = json.load(f)
        print('Going to add {} peers to the Ergo node at {}'.format(len(peers), args.address))
        print()

        for p in peers:
            address = p['address'].replace('/', '')

            print(f'Adding {address} to peer list...', end='')

            params = json.dumps(address).encode('utf8')
            req = ur.Request(url, data=params, headers=headers)
            res = ur.urlopen(req)

            if res.read().decode('utf8') == '"OK"':
                print('OK')
            else:
                print('NOT OK')

            time.sleep(1)
