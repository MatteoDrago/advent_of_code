### PART 1  

file = open('input.txt')

total = 0
valid = 0
for el in file:
    total += 1
    result = el.strip().split(' ')
    limits = result[0].split('-')
    left = int(limits[0])
    right = int(limits[1])
    target = result[1][0]

    occurences = result[2].count(target)
    
    if occurences >= left and occurences <= right:
         valid +=1
         
print(f'There are',valid,'valid passwords over a total of',total)

file.close() 

### PART 2       

file = open('input.txt')

total = 0
valid = 0
for el in file:
    total += 1
    result = el.strip().split(' ')
    limits = result[0].split('-')
    left = int(limits[0]) - 1 
    right = int(limits[1]) - 1
    target = result[1][0]
    
    if (result[2][left] == target) != (result[2][right] == target):
         valid +=1
         
print(f'There are',valid,'valid passwords over a total of',total)

file.close() 
