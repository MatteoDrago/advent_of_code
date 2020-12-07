import numpy as np
### PART 1

file = open('input_05.txt')

total = 0
IDs = []
for el in file:
    el = el.strip()
    bin = ''
    for i in range(0,7):
        if el[i] == 'F':
            bin += '0'
        else:
            bin += '1'
    row = int(bin, 2)
    bin = ''
    for i in range(7,10):
        if el[i] == 'R':
            bin += '1'
        else:
            bin += '0'
    col = int(bin, 2)
    total += 1
    IDs.append(row*8+col)

print(f'We have', total,' boarding passes. Max ID =', np.max(IDs))

IDs.sort()

prev = IDs[0] - 1
for el in IDs:
    if el != (prev + 1):
        miss = el - 1
    prev = el

print('Missing', miss)
