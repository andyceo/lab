#!/usr/bin/env python3

# Extracting Features

def printMatrix(matrix):
  for m in matrix:
    print(m)
  print()

def createMatrix(m, n):
  matrix = []
  for r in range(m):
    matrix.append([])
    for c in range(n):
      matrix[r].append(0)
  return matrix

image = [
[255,  7,  3],
[212,240,  4],
[218,216,230],
]

image = [
[12,18,6],
[2,1,7],
[100,140,130],
]

print('Matrix = ')
printMatrix(image)

# Compute feature matrix for horizontal +|- linear filter
f = createMatrix(3,2)
for n in range(2):
  for m in range(3):
    f[m][n] = image[m][n] - image[m][n + 1]
print('Feature matrix for horizontal linear filter +|- =')
printMatrix(f)
print()

# Compute feature matrix for horizontal -|+ linear filter
f = createMatrix(3,2)
for n in range(2):
  for m in range(3):
    f[m][n] = image[m][n + 1] - image[m][n]
print('Feature matrix for horizontal linear filter -|+ =')
printMatrix(f)
print()

# Compute feature matrix for vertical -|+ linear filter
f = createMatrix(2,3)
for m in range(2):
  for n in range(3):
    f[m][n] = image[m + 1][n] - image[m][n]
print('Feature matrix for vertical linear filter -|+ =')
printMatrix(f)
print()
