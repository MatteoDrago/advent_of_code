import numpy as np

board = np.loadtxt("input_05.txt", dtype="str")
n = 1000 # arbitrary number based on a quick look at the input file

board = np.delete(board, 1, axis=1) 
sea = np.zeros((n,n))

# in this problem from the text we need to consider a tuple as (col, row) 
# which is the opposite with respect to how numpy uses 2D arrays

for el in board:
    start = tuple(map(int,el[0].split(',')))
    end = tuple(map(int,el[1].split(',')))
    if start[0] == end[0]: 
        up = min(start[1], end[1])
        down = max(start[1], end[1])
        
        sea[up:down+1, start[0]] += 1
    elif start[1] == end[1]: 
        sx = min(start[0], end[0])
        dx = max(start[0], end[0])
        
        sea[start[1], sx:dx+1] += 1
    else:
        # iteratively check what is the direction, and update the diagonal accordingly
        a = start
        if start[0] < end[0] and start[1] < end[1]:

            while a != end:
                sea[a[1], a[0]] += 1 
                a = tuple( (a[0] + 1, a[1] + 1))

        elif start[0] < end[0] and start[1] > end[1]:
            
            while a != end:
                sea[a[1], a[0]] += 1 
                a = tuple( (a[0] + 1, a[1] - 1))
                
        elif start[0] > end[0] and start[1] < end[1]:
            
            while a != end:
                sea[a[1], a[0]] += 1 
                a = tuple( (a[0] - 1, a[1] + 1))

        elif start[0] > end[0] and start[1] > end[1]:
            
            while a != end:
                sea[a[1], a[0]] += 1  
                a = tuple( (a[0] - 1, a[1] - 1))

        sea[a[1], a[0]] += 1 

print(len(np.where(sea >= 2)[0]))