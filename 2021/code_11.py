import numpy as np

def propagate(point, z, octopus):
    if point not in z:
            if octopus[point[0], point[1]] == 0:
                z.append(point)
                z = flash_adjacent(point, z, octopus)
            else:
                octopus[point[0], point[1]] = (octopus[point[0], point[1]] + 1) % 10
                if octopus[point[0], point[1]] == 0:
                    z.append(point)
                    z = flash_adjacent(point, z, octopus)

def flash_adjacent(point, z, octopus):
    if point[0] > 0:
        #check up
        c = (point[0]-1,point[1])
        propagate(c,z,octopus)
        
        if point[1] < np.shape(octopus)[1]-1:
            # check up-right diagonal
            c = (point[0]-1,point[1]+1)
            propagate(c,z,octopus)
        
        if point[1] > 0:
            # check up-left diagonal
            c = (point[0]-1,point[1]-1)
            propagate(c,z,octopus)
    
    if point[1] < np.shape(octopus)[1]-1:
        #check right
        c = (point[0],point[1]+1)
        propagate(c,z,octopus)
    
    if point[0] < np.shape(octopus)[0]-1:
        #check down
        c = (point[0]+1,point[1])
        propagate(c,z,octopus)

        if point[1] < np.shape(octopus)[1]-1:
            # check down-right diagonal
            c = (point[0]+1,point[1]+1)
            propagate(c,z,octopus)
        
        if point[1] > 0:
            # check down-left diagonal
            c = (point[0]+1,point[1]-1)
            propagate(c,z,octopus)

    if point[1] > 0:
        #check left
        c = (point[0],point[1]-1)
        propagate(c,z,octopus)
    
    return z

# octopus = np.loadtxt('dummy.txt', dtype=str)
octopus = np.loadtxt('input_11.txt', dtype=str)

# data preprocessing
octopus_m = []
for line in octopus:
    octopus_m.append([int(i) for i in line])
octopus = np.array(octopus_m)

n_steps = 100
count = 0
for step in range(n_steps):
    zeros = []
    octopus = (octopus + 1) % 10
    for i, row in enumerate(octopus):
        for j, col in enumerate(row):
            if col == 0 and (i,j) not in zeros:
                zeros.append((i,j))
                zeros = flash_adjacent((i,j), zeros, octopus)
    count += len(zeros)

print("Answer to first part is ", count)

octopus = np.array(octopus_m)
step = 0
while np.sum(octopus) != 0:
    step += 1
    zeros = []
    octopus = (octopus + 1) % 10
    for i, row in enumerate(octopus):
        for j, col in enumerate(row):
            if col == 0 and (i,j) not in zeros:
                zeros.append((i,j))
                zeros = flash_adjacent((i,j), zeros, octopus)

print("Answer to second part is ", step)
