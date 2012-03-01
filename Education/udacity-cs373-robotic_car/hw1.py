colors = [['red', 'green', 'green', 'red' , 'red'],
          ['red', 'red', 'green', 'red', 'red'],
          ['red', 'red', 'green', 'green', 'red'],
          ['red', 'red', 'red', 'red', 'red']]

measurements = ['green', 'green', 'green' ,'green', 'green']
motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]
sensor_right = 0.7
p_move = 0.8

def show(p):
    for row in p:
        for cell in row:
            print('{:f} '.format(cell), end='')
        print()
    print()




#colors = [['green', 'green' , 'green'],
#          ['green', 'red', 'red'],
#          ['green', 'green', 'green']]
#measurements = ['red', 'red']
#motions = [[0,0], [0,1]]
#sensor_right = 1.0
#p_move = 0.5

#DO NOT USE IMPORT
#ENTER CODE BELOW HERE
#ANY CODE ABOVE WILL CAUSE
#HOMEWORK TO BE GRADED
#INCORRECT

# INITIALIZATION
p = []
sensor_wrong = 1 - sensor_right
p_stay = 1- p_move
cells_quantity = len(colors) * len(colors[0])
init_p = 1.0 / cells_quantity
for m, row in enumerate(colors):
    q = []
    for n, cell in enumerate(row):
        q.append(init_p)
    p.append(q)


def sense(Z):
    buffer = []
    s = 0
    for m, row in enumerate(p):
        q = []
        for n, cell in enumerate(row):
            hit = (Z == colors[m][n])
            mult = (hit * sensor_right + (1-hit) * sensor_wrong)
            q.append(p[m][n] * mult)
        buffer.append(q)
        s += sum(q)
    for m, row in enumerate(buffer):
        for n, cell in enumerate(row):
            buffer[m][n] = buffer[m][n] / s
    return buffer


def move(U):
    buffer = []
    #p_not_move = 1 - p_move
    for m, row in enumerate(p):
        q = []
        for n, cell in enumerate(row):
            pm = (m - U[0]) % len(p)
            pn = (n - U[1]) % len(row)
            s = p_move * p[pm][pn]
            s += p_stay * p[m][n]
            q.append(s)
        buffer.append(q)
    return buffer


#Your probability array must be printed
#with the following code.

print('Initial distrubution')
show(p)
print()

for i in range(len(motions)):
    p = move(motions[i])
    show(p)
    p = sense(measurements[i])
    show(p)
