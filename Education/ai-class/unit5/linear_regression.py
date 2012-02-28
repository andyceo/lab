#!/usr/bin/env python3

x = [1,3,4,5,9]
y = [2,5.2,6.8,8.4,14.8]

#x = [3,6,4,5]
#y = [0,-3,-1,-2]


def calcw1(datax, datay):
    from functools import reduce

    M = len(datax)
    if M != len(datay):
        print('Number of x data = %d not equal to number of y data = %d' % M, len(datay))

    Exy = sum(map(lambda x,y: x*y, datax, datay))
    Ex2 = reduce(lambda res, x: res + x**2, datax, 0)
    Ex = sum(datax)
    Ey = sum(datay)

    print('M = %s' % M)
    print('Exy = %s' % Exy)
    print('Ex = %s' % Ex)
    print('Ey = %s' % Ey)
    print('ExEy = %s' % (Ex * Ey))
    print('Ex2 = %s' % Ex2)
    print('Ex = %s' % Ex)

    w1 = (M*Exy - Ex*Ey) / (M*Ex2 - Ex**2)
    return w1


def calcw0(w1, datax, datay):
    Ey = sum(datay)
    Ex = sum(datax)
    M = len(datax)
    w0 = (1/M) * Ey - (w1/M) * Ex
    return w0

w1 = calcw1(x, y)
w0 = calcw0(w1, x, y)

print ('w0 = %s' % w0)
print('w1 = %s' % w1)
