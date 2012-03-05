def test_n(n):
    for i in range(6):
        if n % 5 != 1:
            return False
        n = n-1
        n = n-(n/5)
    return True

for j in range(100000):
    if test_n(j):
        print j
