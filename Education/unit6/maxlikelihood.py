#!/usr/bin/env python3

# one-dimensional case

data = [3,4,5,6,7]
data = [3,9,9,3]
data = [3,4,5,6,7]
data = [8,7,5,3,2]

def calcMu(data):
    M = len(data)
    return sum(data) / M

def calcSigmasq(data):
    M = len(data)
    mu = calcMu(data)
    sigmasq = sum((x - mu) ** 2 for x in data) / M
    return sigmasq

print('Data:')
print(data)
print('Mu = %s' % calcMu(data))
print('Sigma squared = %s' % calcSigmasq(data))
