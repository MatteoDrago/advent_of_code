import numpy as np
from itertools import permutations

## length = 2 for finding one
## length = 3 for finding seven
## length = 4 for finding four
## length = 7 for finding eight

def find_number(b, length=2):
    for digits in b:
        if len(digits) == length:
            return digits

def find_three(b, signal):
    for digits in b:
        if len(digits) == 5:
            # print(digits, signal)
            if signal[0] in digits and signal[1] in digits and signal[2] in digits:
                return digits

def find_left_side(mapping):
    count = ''
    for c in mapping[8]:
        if c not in mapping[3]:
            count += c
    return count

def find_zero(b, mapping, left):
    for el in b:
        flag = False
        if len(el) == 6:
            for c in mapping[1]+left:
                if c not in el:
                    flag = True
            if not flag:
                return el

def find_nine(b, mapping, left):
    for el in b:
        flag = False
        if len(el) == 6:
            for c in left:
                if c not in el:
                    flag = True
            if flag and mapping[7][0] in el and mapping[7][1] in el and mapping[7][2] in el:
                return el

def find_six(b, mapping, left):
    for el in b:
        flag = False
        if len(el) == 6:
            for c in left:
                if c not in el:
                    flag = True
            if not flag and (el != mapping[9]) and (el != mapping[0]):
                return el

def find_five(b, mapping):
    for el in b:
        flag = False
        if len(el) == 5:
            for c in el:
                if c not in mapping[6]:
                    flag = True
            if (not flag) and (el != mapping[3]):
                return el

def find_two(b, mapping):
    for el in b:
        flag = False
        if len(el) == 5:
            for c in el:
                if c not in mapping[6]:
                    flag = True
            if flag and (el != mapping[3]) and (el != mapping[5]):
                return el

# notes = np.loadtxt('dummy.txt', delimiter='|', dtype=str)
notes = np.loadtxt('input_08.txt', delimiter='|', dtype=str)
unique = [2,4,3,7]

count = 0
for signals in notes[:,1]:
    b = signals.split(' ')[1:]
    for digits in b:
        if len(digits) in unique:
            count+=1

print('Answer first part: ', count)

### MAP ALL NUMBERS
count = 0
for lines in notes:
    mapping = ['', '', '', '', '', '', '', '', '', '']

    b = lines[0].split(' ')
    number = ''
    mapping[1] = find_number(b, 2)
    mapping[7] = find_number(b, 3)
    mapping[4] = find_number(b, 4)
    mapping[8] = find_number(b, 7)
    mapping[3] = find_three(b, mapping[7])
    left = find_left_side(mapping)

    mapping[0] = find_zero(b, mapping, left)
    mapping[9] = find_nine(b, mapping, left)
    mapping[6] = find_six(b, mapping, left)
    mapping[5] = find_five(b, mapping)
    mapping[2] = find_two(b, mapping)

    t = lines[1].split(' ')[1:]

    for el in t:
        perm = [''.join(p) for p in permutations(el)]
        for i,num in enumerate(mapping):
            if num in perm:
                number += str(i)
    
    count += int(number)

print("Answer second part: ", count)