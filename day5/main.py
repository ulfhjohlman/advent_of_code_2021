def countOverlaps(ventMap):
    count = 0
    for col in ventMap:
        for i in col:
            if i > 1:
                count +=1
    print(count)

def getPointsFromLine(line):
    points = []
    xStride = 1 if line[0][0] < line[1][0] else -1
    yStride = 1 if line[0][1] < line[1][1] else -1

    xArr = list(range(line[0][0], line[1][0] + xStride, xStride))
    yArr = list(range(line[0][1], line[1][1] + yStride, yStride))

    if len(xArr) == 1:
        xArr = xArr * len(yArr)
    if len(yArr) == 1:
        yArr = yArr * len(xArr)

    for i in zip(xArr, yArr):
        points.append( [i[0], i[1]])
    return points

def plotVentLines(ventMap, ventLines):
    for line in ventLines:
        points = getPointsFromLine(line)
        for point in points:
            ventMap[point[0]][point[1]] += 1

with open("day5/input") as f:
    # part 1
    ventMap = [1000 * [0] for i in range(1000)]
    ventLines = []
    for line in f:
        points = line.split(" -> ")
        p1 = [int(x) for x in points[0].split(',')]
        p2 = [int(x) for x in points[1].split(',')]

        if(p1[0] == p2[0] or p1[1] == p2[1]):
            ventLines.append([p1, p2])

    plotVentLines(ventMap, ventLines)
    countOverlaps(ventMap)


with open("day5/input") as f:
    # part 2
    ventMap = [1000 * [0] for i in range(1000)]
    ventLines = []
    for line in f:
        points = line.split(" -> ")
        p1 = [int(x) for x in points[0].split(',')]
        p2 = [int(x) for x in points[1].split(',')]

        ventLines.append([p1, p2])
    plotVentLines(ventMap, ventLines)
    countOverlaps(ventMap)
    