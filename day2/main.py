def part1():
    depth = 0
    horizontal_dist = 0
    with open('day2/input', r'r') as f:
        for line in f:
            [num] = [int(x) for x in line.split() if x.isdigit()]
            if 'forward' in line:
                horizontal_dist += num
            elif 'down' in line:
                depth += num
            elif 'up' in line:
                depth = max(0, depth - num)

    print("horizontal_dist", horizontal_dist, " depth: ", depth)
    print("horizontal_dist * depth: ", horizontal_dist * depth)

def part2():
    aim=0
    depth = 0
    horizontal_dist = 0
    with open('day2/input', r'r') as f:
        for line in f:
            [num] = [int(x) for x in line.split() if x.isdigit()]
            if 'forward' in line:
                horizontal_dist += num
                depth += aim * num
            elif 'down' in line:
                aim += num
            elif 'up' in line:
                aim -= num

    print("horizontal_dist", horizontal_dist, " depth: ", depth)
    print("horizontal_dist * depth: ", horizontal_dist * depth)

part1()
part2()