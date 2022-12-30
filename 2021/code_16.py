import numpy as np

BtH = {"0" : "0000", "1" : "0001", "2" : "0010", "3" : "0011", "4" : "0100", "5" : "0101", "6" : "0110", "7" : "0111", "8" : "1000", "9" : "1001", "A" : "1010", "B" : "1011", "C" : "1100", "D" : "1101", "E" : "1110", "F" : "1111"}

def toBinary(pkt):
    new_bits = pkt
    new_bits = new_bits.replace("0", "Z")

    for x in BtH.keys():
        new_bits = new_bits.replace(x, BtH[x])

    new_bits = new_bits.replace("Z", "0000")
    return new_bits

def parsePacket(pkt, packet):

    packet['version'] = int(pkt[0:3], 2)
    packet['type'] = int(pkt[3:6], 2)

    if packet['type'] != 4:
        i = pkt[6]
        if i == '0':
            l = int(pkt[7:22], 2)
            packet['length_ID'] = {'a': int(pkt[6]), 'b':l}
            packet['data'] = []
            start = 22
            while start < 22+l:
                packet['data'].append(parsePacket(pkt[start:start+l], {}))
                start += packet['data'][-1]['length']
            packet['length'] = 22+l
        else:
            n = int(pkt[7:18], 2)
            packet['length_ID'] = {'a': int(pkt[6]), 'b':n}
            packet['data'] = []
            start = 18
            for j in range(n):
                packet['data'].append(parsePacket(pkt[start:], {}))
                start += packet['data'][-1]['length']
            packet['length'] = start
    else:
        start = 6
        lit = 6
        digit = ''

        while pkt[lit] != '0':
            digit += pkt[start+1:start+5] # append only the bits referring to the number (first bit is guard)
            lit += 5
            start += 5

        digit += pkt[start+1:start+5]

        while (len(digit) % 4) != 0: # need this to avoid wrong format
            digit += '0'

        packet['data'] = int(digit,2)
        packet['length'] = lit + 5 # add 5 to ocunt also for the last number 
    
    return packet

def countVersions(packet):
    res = 0
    if packet:
        res += packet['version']

    if isinstance(packet['data'], list):
        for el in packet['data']:
            res+= countVersions(el)
    else:
        if packet['type'] != 4:
            res += countVersions(packet['data'])

    return res

def evaluate(packet):
    if packet['type'] == 0:
        res = 0
        for el in packet['data']:
            res += evaluate(el)
    elif packet['type'] == 1:
        res = 1
        for el in packet['data']:
            res *= evaluate(el)
    elif packet['type'] == 2:
        res = []
        for el in packet['data']:
            res.append(evaluate(el))
        return min(res)
    elif packet['type'] == 3:
        res = []
        for el in packet['data']:
            res.append(evaluate(el))
        return max(res)
    elif packet['type'] == 4:
        return packet['data']
    elif packet['type'] == 5:
        if evaluate(packet['data'][0]) > evaluate(packet['data'][1]):
            return 1
        return 0
    elif packet['type'] == 6:
        if evaluate(packet['data'][0]) < evaluate(packet['data'][1]):
            return 1
        return 0
    elif packet['type'] == 7:
        if evaluate(packet['data'][0]) == evaluate(packet['data'][1]):
            return 1
        return 0

    return res

original = np.array2string(np.loadtxt('input_16.txt', dtype=str))

bits = toBinary(original)
parsed = parsePacket(bits[1:-2], {})
print("Answer to first part is: ", countVersions(parsed))
print("Answer to second part is: ", evaluate(parsed))