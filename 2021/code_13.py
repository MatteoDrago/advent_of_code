import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)

# from the text, you can see that input coordinates are (col, row), opposite than (row, col) from python 
input = open('input_13.txt', mode='r')

coords = []
fold = []
for line in input:
    proc = line.strip().split(',')
    if len(proc) == 2:
        coords.append([int(proc[0]), int(proc[1])])
    if len(proc) == 1 and proc[0] != '':
        instru = proc[0].split('=')
        fold.append((instru[0][-1], int(instru[1])))
        
paper = np.array(coords)

for ins in fold:
    if ins[0] == 'y':
        for line in paper[paper[:,1] > ins[1]]:
            point = [line[0], 2*ins[1]-line[1]]
            if point not in paper.tolist():
                paper = np.insert(paper, -1, point, axis=0)

        paper = np.delete(paper, np.where(paper[:,1] > ins[1]), axis=0)

    elif ins[0] == 'x':
        for line in paper[paper[:,0] > ins[1]]:
            point = [2*ins[1]-line[0], line[1]]
            if point not in paper.tolist():
                paper = np.insert(paper, -1, point, axis=0)

        paper = np.delete(paper, np.where(paper[:,0] > ins[1]), axis=0)

mat = np.zeros((np.max(paper, 0)[1]+1, np.max(paper, 0)[0]+1), dtype=int)
for el in paper:
    mat[el[1], el[0]] = 8

for line in mat:
    line_string = ''
    for el in line:
        if el == 0:
            line_string += '.'
        else:
            line_string += '#' 
    print(line_string)