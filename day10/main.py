def check(line):
    stack = []
    for char in line:
        if char == "]":
            top = stack.pop()
            if top != "[":
                return char
        elif char == "}":
            top = stack.pop()
            if top != "{":
                return char
        elif char == ">":
            top = stack.pop()
            if top != "<":
                return char
        elif char == ")":
            top = stack.pop()
            if top != "(":
                return char
        else:
            stack.append(char)
    return stack

validLines = []
with open("day10/input") as f:
    score = 0
    for line in f:
        ret = check(line)
        if ret == ")":
            score +=3
        elif ret == "]":
            score +=57
        elif ret == "}":
            score +=1197
        elif ret == ">":
            score +=25137
        else:
            validLines.append(ret)

print(score)
print(len(validLines),"valid lines")

def closer(char):
    if char == '[':
        return ']'
    if char == '(':
        return ')'
    if char == '{':
        return '}'
    if char == '<':
        return '>'
    else:
        exit(-1)

scorelist = []
for line in validLines:
    score = 0
    closingLine = [closer(x) for x in reversed(line) if x != "\n"]
    for char in closingLine:
        if char == ')':
            score = score*5 + 1
        if char == ']':
            score = score*5 + 2
        if char == '}':
            score = score*5 + 3
        if char == '>':
            score = score*5 + 4
    scorelist.append(score)

scorelist.sort()
print(scorelist[int(len(scorelist)/2)])