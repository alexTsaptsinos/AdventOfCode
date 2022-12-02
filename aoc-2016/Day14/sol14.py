
f = open("input14.txt","r")
lines = f.readlines()

raceTime = 2503

distances = []

for line in lines:
    lineSplit = line.split()
    reindeerName = lineSplit[0]
    reindeerSpeed = int(lineSplit[3])
    speedLength = int(lineSplit[6])
    restTime = int(lineSplit[13])

    totalTime = speedLength + restTime
    no_cycles = raceTime/totalTime

    wholeCycles = int(no_cycles)
    leftoverTime = raceTime - (wholeCycles*totalTime)
    distance = reindeerSpeed*speedLength*wholeCycles + min(leftoverTime,speedLength)*reindeerSpeed
    distances.append(distance)

print("Maximum Distance:",max(distances))


