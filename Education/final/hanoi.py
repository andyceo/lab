def check_hanoi_stick(s):
    # check if zeros after some disk
    l = 0
    for n in s:
        if l > n: return False
        if n == 0 and l > 0: return False
    return True


s = [0,0,0,0]
res = []

for pos in range(4):
    for v in range(5):
        # we can insert v in pos only if:
        # 1. all values in positions that > pos are less then v
        # 2. all values in positions that < pos are bigger then v
            s[pos] = v
            for pos1 in range(pos+1, 4):
                for v2 in range(5):
                    s[pos1] = v2
                    print(s)
                    #if check_hanoi_stick(s): res.append(s)

#print(res)
