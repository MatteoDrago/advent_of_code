
def bin_to_int(vec=[]):
    max_pow = len(vec)-1
    num = 0
    for i, el in enumerate(vec):
        num += el * (2**(max_pow-i))
    return num