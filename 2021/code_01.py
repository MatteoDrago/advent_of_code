import numpy as np

numbers = np.loadtxt('input_01.txt')

def first_part():
    a = [numbers[i] - numbers[i-1] for i in range(1,len(numbers))]
    b = [x for x in a if x > 0]
    return len(b)

def second_part():
    a = [numbers[i] + numbers[i+1] + numbers[i+2] for i in range(0,len(numbers)-2)]
    b = [a[i] - a[i-1] for i in range(1,len(numbers)-2)]
    c = [x for x in b if x > 0]
    return len(c)

print("Answer first part: ", first_part())
print("Answer second part: ",second_part())