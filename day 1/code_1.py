import numpy as np

def binary_search(target, numb):
    if len(numb) == 0 :
        return False
    if target < numb[0] or target > numb[-1]:
        return False
    mid = int(len(numb) / 2)
    if target == numb[mid]:
        return True
    if target > numb[mid] :
        return binary_search(target,numb[mid:-1])
    else:
        return binary_search(target,numb[0:mid])

numbers = np.loadtxt('input_1.txt')

numbers.sort()

print(numbers)

for i, el in enumerate(numbers):
    miss = 2020 - el
    #print(f'You need', miss)
    found = binary_search(miss, numbers[i+1:-1])
    if found:
        check = el + miss 
        print(f'Starting from',el,'we found',miss,' that sums to ', check)
        print(el * miss)
        
for i, el in enumerate(numbers):
    first = 2020 - el
    for j, le in enumerate(numbers[i+1:-1]):
        miss = first - le
        if miss < 0:
            continue
        found = binary_search(miss, numbers[j+1:-1])
        if found:
            check = el + le + miss 
            print(f'Starting from',el,'and',le,'we found',miss,'that sums to ', check)
            print(el * le * miss)
