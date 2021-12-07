# part 1
with open("day7/input") as f:
    for line in f:
        crabs = [int(x) for x in line.split(",")]
        crabs.sort()
        maxdist = max(crabs)

        fuelCost = [0] * maxdist
        for dist in range(maxdist):
            for c in crabs:
                fuelCost[dist] += abs(c - dist)

        print(min(fuelCost))

# part 2
with open("day7/input") as f:
    for line in f:
        crabs = [int(x) for x in line.split(",")]
        crabs.sort()
        maxdist = max(crabs)

        fuelCost = [0] * maxdist
        for dist in range(maxdist):
            for c in crabs:
                diff = abs(c - dist)
                fuelCost[dist] += (diff * (diff+1)) / 2

        print(min(fuelCost))