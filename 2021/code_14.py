# import numpy as np
# import time

# # polymer = np.loadtxt('dummy.txt', delimiter=' ', skiprows=2, dtype=str)
# # start = np.array2string(np.loadtxt('dummy.txt', dtype='str', max_rows=1)).strip()


# def find_pair(start, get):
#     pattern = start
#     l = len(pattern)
#     if l > 2:
#         half = int(l/2)
#         # left = find_pair(pattern[:half], p_dict) 
#         # right = find_pair(pattern[half:], p_dict)

#         # return ''.join([left,p_dict.get(''.join([left[-1],right[0]]),''),right])

#         return ''.join([find_pair(pattern[:half], get),
#                         get(''.join([pattern[half-1],pattern[half]]),''),
#                         find_pair(pattern[half:], get)])
#     elif l == 2:
#         return ''.join([pattern[0], get(pattern), pattern[1]])
    
#     return pattern

# # def find_pair_dp(start, get, p_dict, lim=2):
# #     i = 0
# #     while i < len(start) - lim + 1:
# #         search = start[i:i+lim+1]
# #         result = get(search,'')
# #         # print(search, result)
# #         if result != '':
# #             start = ''.join([start[:i],result,start[i+2:]])
# #             i += len(result) - 1
# #         elif len(search) == 2:
# #             p_dict[search] = search
# #             i += len(search) - 1
# #         else:
# #             new_item = find_pair_dp(search, get, p_dict, lim=lim-1)
# #             # print('Search for', search, 'found', new_item, 'join with', start)
# #             # print(i, i+lim)
# #             start = ''.join([start[:i],new_item,start[i+lim+1:]])
# #             # print(i, lim, [start[:i],new_item,start[i+lim+1:]])
# #             p_dict[search] = new_item
# #             print('adding', new_item, 'to', search)
# #             i += len(new_item) - 1
# #         # print(i, len(start) - 1)
    
# #     return start
# LIM = 50000

# def find_pair_dp(pattern, p_dict, get):
#     # pattern = start
#     l = len(pattern)
#     if l > LIM:
#         half = int(l/2)
#         # left = find_pair_dp(pattern[:half], p_dict, get)
#         # right = find_pair_dp(pattern[half:], p_dict, get)
#         # check = pattern[half-1:half+1]
#         # return ''.join([left[:len(left)-1],
#         #                 get(check,check),
#         #                 right[1:]])
#         left = find_pair_dp(pattern[:half+1], p_dict, get)
#         right = find_pair_dp(pattern[half:], p_dict, get)
#         return ''.join([left[:len(left)],right[1:]])
#     if l > 2 and l <= LIM:
#         half = int(l/2)
#         result = get(pattern)
#         # print(half, pattern[:half], pattern[half-1],pattern[half])
#         if result:
#             return result
#         else: 
#             left = find_pair_dp(pattern[:half], p_dict, get)
#             right = find_pair_dp(pattern[half:], p_dict, get)
#             check = pattern[half-1:half+1]
#             p_dict[pattern] = ''.join([left[:len(left)-1],
#                                         get(check,check),
#                                         right[1:]])
#             return p_dict[pattern]
#     elif l == 2:
#         return get(pattern, pattern)
#     elif l == 1:
#         return pattern

# # -------------------- #

# steps = 40

# polymer = np.loadtxt('input_14.txt', delimiter=' ', skiprows=2, dtype='str')
# start = np.array2string(np.loadtxt('input_14.txt', dtype=str, max_rows=1)).strip()

# # polymer = np.loadtxt('dummy.txt', delimiter=' ', skiprows=2, dtype='str')
# # start = np.array2string(np.loadtxt('dummy.txt', dtype=str, max_rows=1)).strip()
# start = start[1:-1]
# start_v2 = start

# patt_dict = {}
# patt_dict_dp = {}

# for el in polymer:
#     patt_dict[el[0]] = el[2]

# for el in polymer:
#     patt_dict_dp[el[0]] = el[0][0] + el[2] + el[0][1]

# # b = time.time()

# # print('RECURSION')
# # for s in range(steps):
# #     final = find_pair(start, patt_dict.get)
# #     start = final
# #     print("Step ", s+1)

# # e = time.time()
# # # print(final)
# # print('##################')

# f = time.time()
# final = start_v2
# print('DYNAMIC PROGRAMMING')
# for s in range(steps):
#     f1 = time.time()
#     final = find_pair_dp(final, patt_dict_dp, patt_dict_dp.get)
#     # start_v2 = final
#     f2 = time.time()
#     print("Step ", s+1, len(patt_dict_dp), len(final), f2-f1)

# g = time.time()

# # print(final == final2)

# # print("Recursion Time", e-b, "Dynamic Programming", g-f)

# print("Dynamic Programming", g-f)

# # print(final)
# unique_elements = list(set(final))

# counting = []
# for el in unique_elements:
#     if el != "'":
#         counting.append(final.count(el))

# counting.sort()
# print(counting)
# print("Answer second part : ",counting[-1] - counting[0])

from collections import Counter
import string

lines = [line.strip() for line in open('input_14.txt', 'r').readlines()]
template = lines[0]
rules = [rule.split(' ') for rule in lines[2:]]
rules = {a: (a[0]+c,c+a[1]) for a,b,c in rules}
pairs = [''.join(p) for p in zip(template, template[1:])]

# total the pairs created by substitution
def run(steps):
    ctr = Counter(pairs)
    print(ctr, rules)
    for i in range(steps):
        newCtr = {key : 0 for key in rules.keys()}
        for key, value in ctr.items():
            newCtr[rules[key][0]] += value
            newCtr[rules[key][1]] += value
        ctr = newCtr

    letterTotals = {letter : 0 for letter in list(string.ascii_uppercase)}
    print(ctr.items())
    for key, value in ctr.items():
        letterTotals[key[0]] += value 

    # the last character in the template gets another count
    letterTotals[template[-1]] += 1

    lmax = max(letterTotals.values())
    lmin = min([value for value in letterTotals.values() if value > 0])
    return lmax - lmin

print('part 1:', run(10))
print('part 2:', run(40))
