#!/usr/bin/env python3

# Monte-Carlo Localization

from math import cos, sin, pi

def calc_x(x0, v, dt, theta):
  x = x0 + v*dt*cos(theta)
  return x

def calc_y(y0, v, dt, theta):
  y = y0 + v*dt*sin(theta)
  return y

def calc_theta(theta0, w, dt):
  theta = theta0 + w*dt
  return theta

# set initial state (t = 0)
x0 = 0
y0 = 0
theta0 = 0

# settings parameters
dt = 4
v = 10
w = pi / 8

for i in range(1,5):
  print('Attempt %s' % i)
  x0 = calc_x(x0, v, dt, theta0)
  y0 = calc_y(y0, v, dt, theta0)
  theta0 = calc_theta(theta0, w, dt)
  print('x = %f' % x0)
  print('y = %f' % y0)
  print('theta = %f' % theta0)
  print('')
