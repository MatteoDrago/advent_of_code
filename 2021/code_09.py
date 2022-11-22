import numpy as np

# smoke = np.loadtxt('dummy.txt', dtype=str)
smoke = np.loadtxt('input_09.txt', dtype=str)

# data preprocessing
smoke_m = []
for line in smoke:
    smoke_m.append([int(i) for i in line])
smoke = np.array(smoke_m)

lowest = []
coordinates = []
for i,line in enumerate(smoke):
    for j,el in enumerate(line):
        if i == 0:
            if j == 0:
                if el < line[j+1] and el < smoke[i+1,j]:
                    lowest.append(el)
                    coordinates.append((i,j))
            elif j == (len(line)-1):
                if el < line[j-1] and el < smoke[i+1,j]:
                    lowest.append(el)
                    coordinates.append((i,j))
            else:
                if el < line[j-1] and el < line[j+1] and el < smoke[i+1,j]:
                    lowest.append(el)
                    coordinates.append((i,j))
        elif i == (len(smoke)-1):
            if j == 0:
                if el < line[j+1] and el < smoke[i-1,j]:
                    lowest.append(el)
                    coordinates.append((i,j))
            elif j == (len(line)-1):
                if el < line[j-1] and el < smoke[i-1,j]:
                    lowest.append(el)
                    coordinates.append((i,j))
            else:
                if el < line[j-1] and el < line[j+1] and el < smoke[i-1,j]:
                    lowest.append(el)
                    coordinates.append((i,j))
        else:
            if j == 0:
                if el < line[j+1] and el < smoke[i-1,j] and el < smoke[i+1,j]:
                    lowest.append(el)
                    coordinates.append((i,j))
            elif j == (len(line)-1):
                if el < line[j-1] and el < smoke[i-1,j] and el < smoke[i+1,j]:
                    lowest.append(el)
                    coordinates.append((i,j))
            else:
                if el < line[j-1] and el < line[j+1] and el < smoke[i-1,j] and el < smoke[i+1,j]:
                    lowest.append(el)
                    coordinates.append((i,j))

print("Answer first part: ", sum(lowest)+1*len(lowest))

def check_borders(smoke, coord, check_M):
    b = []
    if coord[0] > 0:
        #check up
        c = (coord[0]-1,coord[1])
        if smoke[c[0], c[1]] < 9 and check_M[c[0], c[1]] == 0:
            b.append(c)
            check_M[c[0], c[1]] += 1
            b = b + check_borders(smoke, c, check_M)
    if coord[1] < np.shape(smoke)[1]-1:
        #check right
        c = (coord[0],coord[1]+1)
        if smoke[c[0], c[1]] < 9 and check_M[c[0], c[1]] == 0:
            b.append(c)
            check_M[c[0], c[1]] += 1
            b = b + check_borders(smoke, c, check_M)
    if coord[0] < np.shape(smoke)[0]-1:
        #check down
        c = (coord[0]+1,coord[1])
        if smoke[c[0], c[1]] < 9 and check_M[c[0], c[1]] == 0:
            b.append(c)
            check_M[c[0], c[1]] += 1
            b = b + check_borders(smoke, c, check_M)
    if coord[1] > 0:
        #check left
        c = (coord[0],coord[1]-1)
        if smoke[c[0], c[1]] < 9 and check_M[c[0], c[1]] == 0:
            b.append(c)
            check_M[c[0], c[1]] += 1
            b = b + check_borders(smoke, c, check_M)
    return b

basins_size = []
for coord in coordinates:
    check_M = np.zeros(np.shape(smoke))
    check_M[coord[0], coord[1]] += 1
    basin = check_borders(smoke, coord, check_M) + [coord]
    basins_size.append(len(basin))

basins_size.sort()
print("Answer second part: ", basins_size[-1]*basins_size[-2]*basins_size[-3])