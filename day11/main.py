from os import X_OK


dumbos = []
flashes = 0

def incAll(dumbos):
    for i, r in enumerate(dumbos):
        for j, x in enumerate(r):
            dumbos[i][j] +=1


def incAdj(i,j,dumbos):
    N = len(dumbos)
    for x in range(max(0,i-1),min(i+1,N-1)+1):
        for y in range(max(0,j-1),min(j+1,N-1)+1):
            if(x != i or y != j):
                dumbos[x][y] += 1

def resetDumbos(dumbos):
    for i, row in enumerate(dumbos):
        for j, x in enumerate(row):
            if x > 9:
                dumbos[i][j] = 0

def handleFlashes(dumbos):
    numFlashesThisIter = 0
    newFlash = True
    N =len(dumbos)
    hasFlashed = [ [0] * N for _ in range(N)]

    while(newFlash == True):
        newFlash = False
        for i, row in enumerate(dumbos):
            for j, num in enumerate(row):
                if num > 9 and not hasFlashed[i][j]:
                    numFlashesThisIter += 1
                    hasFlashed[i][j] = True
                    incAdj(i, j, dumbos)
                    newFlash = True
    return numFlashesThisIter

with open("day11/input") as f:
    for line in f:
        dumbos.append([int(x) for x in line if x != "\n"])

for i in range(1,101):
    incAll(dumbos)
    numFlashesThisIter = handleFlashes(dumbos)
    flashes += numFlashesThisIter
    resetDumbos(dumbos)

print(flashes)
#part2
for i in range(101,1000):
    incAll(dumbos)
    numFlashesThisIter = handleFlashes(dumbos)
    flashes += numFlashesThisIter
    resetDumbos(dumbos)
    if(numFlashesThisIter == 100):
        print("It's happening! Iter:", i)
        break
