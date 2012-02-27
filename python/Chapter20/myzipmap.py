def myzip(*seqs):
    seqs = [list(s) for s in seqs]
    res = []
    while all(seqs):
        res.append(tuple(s.pop(0) for s in seqs))
    return res

def mymapPad(*seqs, pad = None):
    seqs = [list(s) for s in seqs]
    res = []
    while any(seqs):
        res.append(tuple((s.pop(0) if s else pad) for s in seqs))
    return res

print('Illustrate regular functions')
s1, s2 = 'abc', 'xyz123'
print(myzip(s1,s2))
print(mymapPad(s1,s2))
print(mymapPad(s1,s2,pad=99))


def myzipgen(*seqs):
    seqs = [list(s) for s in seqs]
    while all(seqs):
        yield tuple(s.pop(0) for s in seqs)

def mymapPadgen(*seqs, pad=None):
    seqs = [list(s) for s in seqs]
    while any(seqs):
        yield tuple((s.pop(0) if s else pad) for s in seqs)

print('Illustrate generator functions')
s1, s2 = 'abc', 'xyz123'
print(list(myzipgen(s1,s2)))
print(list(mymapPadgen(s1,s2)))
print(list(mymapPadgen(s1,s2,pad=99)))


def myzipalt(*seqs):
    minlen = min(len(s) for s in seqs)
    return [tuple(s[i] for s in seqs for i in range(minlen))]

def mymapPadalt(*seqs, pad = None):
    maxlen = max(len(s) for s in seqs)
    index = range(maxlen)
    return [tuple((s[i] if len(s) > i else pad) for s in seqs) for i in index]

print('Illustrate alternate functions')
s1, s2 = 'abc', 'xyz123'
print(list(myzipalt(s1,s2)))
print(list(mymapPadalt(s1,s2)))
print(list(mymapPadalt(s1,s2,pad=99)))
