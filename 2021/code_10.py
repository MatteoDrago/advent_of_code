import numpy as np

syntax = np.loadtxt("dummy.txt", dtype = str)
syntax = np.loadtxt("input_10.txt", dtype = str)

illegal = []
incomplete_score = []

for line in syntax:
    flag = False
    story = []
    expected = ''
    for i,c in enumerate(line):
        if c == '(': 
            expected = ')'
            story.append(c)
        elif c == '[':
            expected = ']'
            story.append(c)
        elif c == '{':
            expected = '}'
            story.append(c)
        elif c == '<':
            expected = '>'
            story.append(c)
        elif c != expected and i != 0:
            illegal.append(c)
            flag = True
            break
        elif c == expected and i != 0:
            del story[-1]
            if len(story) > 0:
                c = story[-1]
                if c == '(': 
                    expected = ')'
                elif c == '[':
                    expected = ']'
                elif c == '{':
                    expected = '}'
                elif c == '<':
                    expected = '>'
    if not flag:
        score = 0
        story.reverse()
        for el in story:
            if el == '(': 
                score = score * 5 + 1
            elif el == '[':
                score = score * 5 + 2
            elif el == '{':
                score = score * 5 + 3
            elif el == '<':
                score = score * 5 + 4
    
        incomplete_score.append(score)

count = 0     
for c in illegal:
    if c == ')': 
        count += 3
    elif c == ']':
        count += 57
    elif c == '}':
        count += 1197
    elif c == '>':
        count += 25137

print("Answer first part: ", count)

incomplete_score.sort()
print("Answer second part: ", incomplete_score[int(len(incomplete_score)/2)])