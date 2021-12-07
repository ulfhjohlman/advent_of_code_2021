with open("day6/input") as f:
    for line in f:
        fish = [int(x) for x in line.split(',')]
        for day in range(80):
            for i in range(len(fish)):
                if fish[i] == 0:
                    fish[i] = 6
                    fish.append(8)
                else:
                    fish[i] -=1

        print(len(fish))

with open("day6/input") as f:
    for line in f:
        fish = [int(x) for x in line.split(',')]
        fishCompressed = [0] * 9
        for i in fish:
            fishCompressed[i] += 1
        for day in range(256):
            newFish = fishCompressed[0]
            for i in range(len(fishCompressed)):
                if i == len(fishCompressed) - 1:
                    fishCompressed[i] = newFish
                else:
                    fishCompressed[i] = fishCompressed[i+1]
                if i == 6:
                    fishCompressed[i] += newFish
        print(sum(fishCompressed))