# variant 1
def show(p):
     for i in range(len(p)):
         for w in range(len(p[0])):
             print "%.4f" % p[i][w],
         print '.' * 45
     print '.' * 80


# variant 2
def show(p):
     for i in range(len(p)):
         for w in range(len(p[0])):
             print "%.4f" % p[i][w],
         print
     print


# variant 3
def show(p):
    for row in p:
        for element in row:
            print "%.4f" % element,
        print
    print
