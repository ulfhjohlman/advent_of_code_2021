with open("day9/input") as f:
    height_map = []
    for line in f:
        height_map.append([int(x) for x in line if x != "\n"])

riskSum = 0
lowPoints = []
for i, row in enumerate(height_map):
    for j, col in enumerate(row):
        thisHeight = height_map[i][j]
        if 0 < i:
            if height_map[i-1][j] <= thisHeight:
                continue
        if i < len(height_map) - 1:
            if height_map[i+1][j] <= thisHeight:
                continue
        if 0 < j:
            if height_map[i][j-1] <= thisHeight:
                continue
        if j < len(height_map[i]) - 1:
            if height_map[i][j+1] <= thisHeight:
                continue
        riskSum += height_map[i][j] + 1
        lowPoints += [(i,j)]
print(riskSum)

def getNeighbourPoints(i,j):
    res = []
    if i > 0:
        res += [(i-1,j)]
    if len(height_map)-1 > i:
        res += [(i+1,j)]
    if j > 0:
        res += [(i,j-1)]
    if len(height_map[0])-1 > j:
        res += [(i,j+1)]
    return res

def getHeigherNeighbourPoints(basin):
    res = []
    for point in basin:
        i = point[0]
        j = point[1]
        height = height_map[i][j]
        neighbourPoints = getNeighbourPoints(i,j)
        for n in neighbourPoints:
            nHeight = height_map[n[0]][n[1]]
            if nHeight != 9 and nHeight >= height:
                if n not in basin:
                    res.append(n)
    return res

basinSizes = []
for point in lowPoints:
    basin = [point]
    basinSize = -1
    while(basinSize != len(basin)):
        basinSize = len(basin)
        for newPoint in getHeigherNeighbourPoints(basin):
            if newPoint not in basin:
                basin.append(newPoint)
    basinSizes += [basinSize]

basinSizes.sort()
print(basinSizes[-1] * basinSizes[-2] * basinSizes[-3])