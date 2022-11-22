import numpy as np
from utils import *

def find_digits(diagno):
    dig = np.zeros(len(diagno[0]))
    for el in diagno:
        for i,j in enumerate(el):
            dig[i] += int(j)
    return dig

def first_part(digits, limit):
    gamma = bin_to_int([round(x/limit) for x in digits])
    epsilon = bin_to_int([1 - round(x/limit) for x in digits])
    return gamma*epsilon

def second_part(digits, diagno):
    oxygen = []
    co2 = []

    for id in digits:
        element = id / len(diagno)
        if element == 0.5:
            oxygen.append(1)
            co2.append(0)
        else:
            oxygen.append(round(element))
            co2.append(1-round(element))

    diagno_ox = diagno.copy()
    diagno_co2 = diagno.copy()
    remaining_ox = []
    remaining_co2 = []

    for i in range(len(digits)):

        if len(remaining_ox) != 1:
            remaining_ox = [x for x in diagno_ox if int(x[i]) == oxygen[i]]
            diagno_ox = remaining_ox
            digits = find_digits(diagno_ox)

            oxygen = []
            for id in digits:
                element = id / len(diagno_ox)
                if element == 0.5:
                    oxygen.append(1)
                else:
                    oxygen.append(round(element))

        if len(remaining_co2) != 1:
            remaining_co2 = [x for x in diagno_co2 if int(x[i]) == co2[i]]
            diagno_co2 = remaining_co2
            digits = find_digits(diagno_co2)

            co2 = []
            for id in digits:
                element = id / len(diagno_co2)
                if element == 0.5:
                    co2.append(0)
                else:
                    co2.append(1 - round(element))

    return bin_to_int([int(x) for x in diagno_ox[0]]) * bin_to_int([int(x) for x in diagno_co2[0]])

diagno = np.loadtxt('input_03.txt', dtype=str)
digits = find_digits(diagno)

print("Answer first part: ", first_part(digits, len(diagno)))
print("Answer second part: ",second_part(digits, diagno))