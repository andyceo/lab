#import module1
#import module2

def func1():
    x = 1
    def func2():
        x = 2
        return x

res = func1()
print(res)
# None

res = func2()
print(res)
# NameError: name func2 not defined

print('end')
# not printing due to error