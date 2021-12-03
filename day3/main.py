def part1():
    with open("day3/input",'r') as f:
        count = {}
        numLines = 0
        for line in f:
            numLines += 1
            for idx, stringX in enumerate(line):
                if stringX.isdigit():
                    x = int(stringX)
                    if idx in count:
                        count[idx] +=x
                    else:
                        count[idx] = x
        gamma_bin = ''
        epsilon_bin = ''
        for k,v in count.items():
            x = (int(0.5 + v / numLines))
            gamma_bin += str(x)
            epsilon_bin += str(1-x)
        print(gamma_bin, epsilon_bin)
        gamma = int(gamma_bin,2)
        epsilon = int(epsilon_bin,2)
        print(gamma, epsilon)
        print(gamma * epsilon)

def part2():
    with open('day3/input') as f:
        arr = []
        for line in f:
            arr.append(line)

        lineLength = len(arr[0]) -1 # minus newline char

        oxygen_gen_group = arr
        for i in range(lineLength):
            oxygen_gen_group = criteriaSelector(oxygen_gen_group, i, 1, 1)
            if(len(oxygen_gen_group) == 1):
                print(oxygen_gen_group)
                break

        co2_scrubber_group = arr
        for i in range(lineLength):
            co2_scrubber_group = criteriaSelector(co2_scrubber_group, i, 0, 0)
            if(len(co2_scrubber_group) == 1):
                print(co2_scrubber_group)
                break

        print(int(oxygen_gen_group[0],2) * int(co2_scrubber_group[0],2))

def criteriaSelector(inputArr, bitPos, keepMostCommon, tieBreaker):
    group0 = []
    group1 = []
    for line in inputArr:
        if line[bitPos] == '0':
            group0.append(line)
        else:
            group1.append(line)

    if len(group0) == len(group1):
        if tieBreaker == 0:
            return group0
        else:
            return group1
    if len(group0) > len(group1):
        if keepMostCommon:
            return group0
        else:
            return group1
    # group1 > group0
    if keepMostCommon:
        return group1
    else:
        return group0

part1()
part2()