import sys
from pathlib import Path
file = Path(__file__).resolve()
root = file.parents[1]
sys.path.append(str(root))

from util.parser import Parser

p = Parser('day1/input')
arr = p.parseNumColumn()

def part1():
    print("len(arr): ", len(arr))

    depthIncreaseCount = 0
    for measureIdx in range(len(arr)):
        currentMeasure = arr[measureIdx]
        if measureIdx > 0 and currentMeasure > previousMeasure:
            depthIncreaseCount = depthIncreaseCount + 1

        previousMeasure = currentMeasure

    print("Depth increases: {}".format(depthIncreaseCount))

def part2():
    depthIncreaseCount = 0
    for measureIdx in range(2,len(arr)):
        currentMeasure = arr[measureIdx] + arr[measureIdx - 1] + arr[measureIdx - 2]
        if measureIdx !=2 and currentMeasure > previousMeasure:
            depthIncreaseCount = depthIncreaseCount + 1

        previousMeasure = currentMeasure

    print("Sliding Depth increases: {}".format(depthIncreaseCount))

def part2_better():
    count = 0
    arr_length = len(arr)
    offset = 3
    for idx, val in enumerate(arr):
        if idx + offset < arr_length:
            if val < arr[idx + offset]:
                count +=1

    print("Sliding depth increases: {}".format(count))

def part1_compact():
    print("Depth increases: {}".format(sum(y > x for x,y in zip(arr[:-1], arr[1:]))))


def part2_compact():
    print("Sliding depth increases: {}".format(sum(y > x for x,y in zip(arr[:-3], arr[3:]))))

part1()
part2()
part2_better()
part1_compact()
part2_compact()
