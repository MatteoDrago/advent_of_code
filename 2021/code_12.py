import numpy as np

def create_connections(caves):
    tunnels = {}
    for line in caves:
        if line[0] not in tunnels.keys():
            tunnels[line[0]] = [line[1]]
        else:
            if line[1] not in tunnels[line[0]] and line[1] != 'start':
                 tunnels[line[0]].append(line[1])
        
        if line[1] not in tunnels.keys():
            tunnels[line[1]] = [line[0]]
        else:
            if line[0] not in tunnels[line[1]] and line[0] != 'start':
                 tunnels[line[1]].append(line[0])
    
    return tunnels

def find_path(key, tunnels, path = []):

    p = path.copy()
    a = 0

    p.append(key)

    for step in tunnels[key]:
        if step == 'start':
            continue
        elif step == 'end':
            print("Found END", p+['end'])
            a += 1
        elif step.islower() and step in p:
            continue
        else:
            a += find_path(step, tunnels, p)

    return a

def find_path_v2(key, tunnels, path = [], small = 0):

    p = path.copy()
    a = 0

    p.append(key)

    for step in tunnels[key]:
        if step == 'start':
            continue
        elif step == 'end':
            a += 1
        elif step.islower(): 
            if step in p:
                if small == 1:
                    continue
                elif small == 0:
                    a += find_path_v2(step, tunnels, p, 1)
            else:
                a += find_path_v2(step, tunnels, p, small)
        else:
            a += find_path_v2(step, tunnels, p, small)

    return a


caves = np.loadtxt("input_12.txt", delimiter='-', dtype=str)
tunnels = create_connections(caves)

count = find_path_v2('start', tunnels, path = [])

print(count)
