import numpy as np


x_lims = [241, 275]
y_lims = [-75, -49]

def in_target(coord):
    return (coord[0] >= x_lims[0] and coord[0]<=x_lims[1]) and (coord[1] >= y_lims[0] and coord[1]<=y_lims[1])

def out_of_target(coord):
    return coord[1] < y_lims[0]

def move_probe(p, s):
    p[0] += s[0]
    p[1] += s[1]

    if s[0] > 0:
        s[0] -= 1

    s[1] -= 1 

# objective function
def objective(s):
    p = [0, 0]
    steps = []
    while not out_of_target(p):
        steps.append(p[1])
        if in_target(p):
            return True, max(steps)
        move_probe(p,s)
    return False, 0


x_min = 0
x_max = x_lims[1] + 1

y_min = y_lims[0] - 1
y_max = (-y_lims[0])*2

def random_search():
    max = 0
    old = []
    sold = []
    for x in range(x_min, x_max):
        for y in range(y_min, y_max):
            speed = [x, y]

            old.append(speed)
            check, res = objective([x for x in speed])
            if check:
                sold.append(speed)
                if res > max:
                    max = res

    return max, len(sold)

nums = (x_max-x_min)*(y_max - y_min)
print("Iterate over", nums, "alternatives")
print(random_search())