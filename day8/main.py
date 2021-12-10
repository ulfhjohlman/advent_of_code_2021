with open("day8/input") as f:
    count = 0
    codeslist = []
    outputlist = []
    for line in f:
        [codes, output] = line.split("|")
        codes = codes.split()
        output = output.split()

        codeslist.append(codes)
        outputlist.append(output)
    for row in outputlist:
        for i in row:
            if (len(i) == 2) or (len(i) == 3) or (len(i) == 4) or (len(i) == 7):
                count+=1

    print(count)

def getCharsInDigit(codes, decoded_codes, digit):
    return codes[decoded_codes.index(digit)]

def decode(input):
    [codes, output] = input.split("|")
    codes = codes.split()

    codes_tmp = []
    for string in codes:
        sorted_characters = sorted(string)
        codes_tmp.append("".join(sorted_characters))
    codes = codes_tmp

    output = output.split()
    output_tmp = []
    for string in output:
        sorted_characters = sorted(string)
        output_tmp.append("".join(sorted_characters))
    output = output_tmp

    decoded_codes = 10 * [-1]
    for k,i in enumerate(codes):
        if len(i) == 3:
            decoded_codes[k] = 7
        if len(i) == 2:
            decoded_codes[k] = 1
        if len(i) == 4:
            decoded_codes[k] = 4
        if len(i) == 7:
            decoded_codes[k] = 8
    for k,i in enumerate(codes):
        if len(i) == 5:
            onesSegments = getCharsInDigit(codes, decoded_codes, 1)
            if onesSegments[0] in i and onesSegments[1] in i:
                decoded_codes[k] = 3
    for k,i in enumerate(codes):
        if len(i) == 6:
            charsNotFound = []
            for char in i:
                if char not in getCharsInDigit(codes, decoded_codes, 3):
                    charsNotFound.append(char)
                    if len(charsNotFound) > 1:
                        break
            if len(charsNotFound) == 1:
                decoded_codes[k] = 9
                break
    for k,i in enumerate(codes):
        if len(i) == 5 and decoded_codes[k] == -1:
            if charsNotFound[0] in i:
                decoded_codes[k] = 5
    for k,i in enumerate(codes):
        if len(i) == 5 and decoded_codes[k] == -1:
            decoded_codes[k] = 2
    for k,i in enumerate(codes):
        if len(i) == 6 and decoded_codes[k] == -1:
            if onesSegments[0] in i and onesSegments[1] in i:
                decoded_codes[k] = 0
    for k,i in enumerate(codes):
        if decoded_codes[k] == -1:
            decoded_codes[k] = 6
    res = ""
    for i in output:
        res += str(decoded_codes[codes.index(i)])
    print(res)
    return int(res)

with open("day8/input") as f:
    count = 0
    for line in f:
        count += decode(line)
    print(count)