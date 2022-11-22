import numpy as np

crabs = np.loadtxt("input_07.txt", delimiter=',', dtype=int)

min_crabs = np.min(crabs)
max_crabs = np.max(crabs)

fuel = []
for el in range(min_crabs, max_crabs+1):
    fuel.append(np.sum(abs(crabs - el)))

print(np.min(fuel))

fuel = []
for el in range(min_crabs, max_crabs+1):
    temp = abs(crabs - el)
    for i,t in enumerate(temp): 
        temp[i] = t*(t+1)/2 # apply gauss formula
    fuel.append(np.sum(temp))

print(np.min(fuel))