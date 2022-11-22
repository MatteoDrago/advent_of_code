import numpy as np

school = np.loadtxt("input_06.txt", dtype=int, delimiter=',')
days = 256

def descendants(start, s, days):
    des = 0
    while s < days:
        if start == 0:
            if (days - (s + 3)) > 6:
                des += descendants(6,s+3, days) + 1
            else: 
                des += 1
            start = 6
            s += 1
            remaining = days - s
            if remaining > start: 
                s += start
                start = 0
            else: 
                return des
        else:
            remaining = days - s
            if remaining > start: 
                s += start
                start = 0
            else: 
                return des
    # print("Descendants ", des)
    return des

tot = len(school)
seen_num = list(np.zeros(8))
seen = []
for el in school:
    print("Check for ", el)
    if el in seen:
        print("Already here ", seen_num[el-1], " descendants")
        tot += seen_num[el-1]
    else:
        num = descendants(el-1, 1, days)
        tot += num
        seen.append(el)
        seen_num[el-1] = num
    

print(tot)

# ITERATIVE SOLUTION (not time feasible)
# start = len(school)
# for i in range(days):
#     for j in range(0,start):
#         if school[j] == 0:
#             school[j] = 6
#             school = np.append(school, 8)
#             start += 1
#         else:
#             school[j] -= 1
# print(len(school))