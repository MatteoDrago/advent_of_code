import numpy as np

travel = np.loadtxt('input_02.txt', dtype={'names': ('dir', 'q'), 'formats':('S1', int)})

def first_part():
    forward = 0
    down = 0
    for el in travel:
        if el[0] == b'f':
            forward += el[1]
        elif el[0] == b'u':
            down -= el[1]
        else:
            down += el[1]
    return forward*down

def second_part():
    forward = 0
    down = 0
    aim = 0
    for el in travel:
        if el[0] == b'f':
            forward += el[1]
            down += aim*el[1]
        elif el[0] == b'u':
            aim -= el[1]
        else:
            aim += el[1]
    return forward*down

print("Answer first part: ", first_part())
print("Answer second part: ",second_part())