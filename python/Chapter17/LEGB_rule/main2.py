g = 10

def func1():
    x = 1
    def func2():
        #x = 2 + x # UnboundLocalError: local variable 'x' referenced before asignment
        #return x
        y = 2 + x
        return y
    return func2

res = func1()
print(res)
# <function func2 at 0x1234567>

res = res()
print(res)
# 3