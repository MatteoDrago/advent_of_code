import numpy as np
import time

def find_neighbours(node, lim):
    neigh = []
    if node[0] < lim[0]:
        neigh.append((node[0]+1, node[1]))
    
    if node[1] < lim[1]:
        neigh.append((node[0], node[1]+1))
    
    if node[0] > 0:
        neigh.append((node[0]-1, node[1]))
    
    if node[1] > 0:
        neigh.append((node[0], node[1]-1))

    return neigh

def dijkstra(graph, node):

    sizes = np.shape(graph)

    visited = {}
    visited[node] = 0

    distances = np.array(np.ones(sizes)*np.infty)
    distances[node[0], node[1]] = 0

    end = (sizes[0]-1, sizes[1]-1)

    while len(visited) > 0 and node != end:
        node = min(visited, key=visited.get)
        del visited[node]
        neighbours = find_neighbours(node, end)
        
        for n in neighbours:
            new_dist = graph[n[0], n[1]] + distances[node[0], node[1]]
            if distances[n[0], n[1]] > new_dist:
                distances[n[0], n[1]] = new_dist
                visited[n[0], n[1]] = new_dist

    return distances[end[0], end[1]]

def tiling(graph, num_tiles, ax):
    tile = graph
    for i in range(num_tiles-1): 
        tile = (tile+1)%10
        zeros = np.where(tile == 0) # find where it is zero
        for j, el in enumerate(zeros[0]):
            tile[el, zeros[1][j]] = 1
        graph = np.concatenate((graph, tile), axis=ax)
    return graph

caverns_txt = np.loadtxt('input_15.txt', dtype=str)
caverns = []
for line in caverns_txt:
    row = [int(x) for x in line]
    caverns.append(row)

source = (0,0)
caverns = np.array(caverns)

a = time.time()
risk = dijkstra(caverns, source)
b = time.time()
print("Answer first part: ", risk, " Time: ", b - a)

caverns = tiling(caverns, 5, 0) # add tiles below
caverns = tiling(caverns, 5, 1) # add tiles on the right

a = time.time()
risk = dijkstra(caverns, source)
b = time.time()
print("Answer second part: ", risk, " Time: ", b - a)