### PART 1

file = open('input_06.txt')

customs = []
count_cust = []
for el in file:
    el = el.strip()
    if el == "":
        count_cust.append(len(customs))
        customs = []
    else:
        for c in el:
            if c not in customs:
                customs.append(c)

if len(customs) > 0:
    count_cust.append(len(customs))
    customs = []

file.close()

print(sum(count_cust))

### PART 2

file = open('input_06.txt')

customs = []
count_cust = []
counter = 0
for el in file:
    el = el.strip()
    if el == "":
        count_cust.append(len(customs))
        customs = []
        counter = 0
    else:
        temp = []
        for c in el:
            temp.append(c)
        if counter == 0:
            customs = temp
        else:
            new_custom = []
            for l in temp:
                if l in customs:
                    new_custom.append(l)
            customs = new_custom
        counter += 1

if len(customs) > 0:
    count_cust.append(len(customs))
    customs = []

file.close()

print(sum(count_cust))
