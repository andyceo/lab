import sys, mytimeradv
from math import sqrt
reps = 10000
repslist = range(reps)

def fSqrt():
    res = []
    for x in repslist:
        res.append(sqrt(x))
    return res

def fStars():
    res = []
    for x in repslist:
        res.append(x ** 0.5)
    return res

def fPow():
    res = []
    for x in repslist:
        res.append(pow(x, 0.5))
    return res

print(sys.version)
for tester in (mytimeradv.timer, mytimeradv.best):
    print('<%s>' % tester.__name__)
    for test in (fSqrt, fStars, fPow):
        elapsed, result = tester(test)
        print('-' * 35)
        print('%-9s: %.5f => [%s...%s]' %
            (test.__name__, elapsed, result[0], result[-1]))

