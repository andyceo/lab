from print30 import print30
print30(1,2,3)
print30(1,2,3,sep='')
print30(1,2,3,sep='...')
print30(1,[2],(3,),sep='...')

print30(4,5,6, sep='', end='')
print30(7,8,9)
print30()

import sys
print30(1,2,3,sep='??', end='.\n', file=sys.stderr)
