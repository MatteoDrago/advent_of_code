### PART 1  

file = open('input_03.txt')

camp = []

for el in file:
    temp_list = []
    temp_list.append(el.strip()*323)
    camp.append(el.strip()*323)
    
file.close()

count = 0
row = 1
col = 3
while(row < 323):
    if (camp[row][col] == '#'):
        count += 1
    row += 1
    col += 3

print(f'PART 1 : Number of trees encountered', count)

### PART 2

row_list = [1,1,1,1,2]
col_list = [1,3,5,7,1]

result = 1
for i in range(len(row_list)):
    count = 0
    row = row_list[i]
    col = col_list[i]
    while(row < 323):
        if (camp[row][col] == '#'):
            count += 1
        row += row_list[i]
        col += col_list[i]
    print(f'PART 2: Number of trees encountered', count)
    result *= count

print(f'Result:',result)
