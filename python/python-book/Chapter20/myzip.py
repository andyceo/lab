# this function illustrates infinite loop in python3.

def myzip(*args):
    iters = map(iter, args) # change to iters = list(map(iter, args)) to work properly in python3
    #print(iters)
    #print([next(i) for i in iters])
    #print(iters)
    #print([next(i) for i in iters])
    #exit(0)
    #c = 0
    while iters:
        #c += 1
        #if c > 4: exit(0)
        res = [next(i) for i in iters]
        #print(res)
        #print(c)
        yield tuple(res)

temp = list(myzip('abc', 'lmnop'))
print(temp)