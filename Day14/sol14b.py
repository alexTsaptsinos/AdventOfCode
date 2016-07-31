
f = open("input14.txt","r")
lines = f.readlines()

raceTime = 2503

names = []
dictionary = {}
for line in lines:
    lineSplit = line.split()
    reindeerName = lineSplit[0]
    dictionary[reindeerName] = {}
    names.append(reindeerName)
    reindeerSpeed = int(lineSplit[3])
    speedLength = int(lineSplit[6])
    restTime = int(lineSplit[13])
    dictionary[reindeerName]["speed"] = reindeerSpeed
    dictionary[reindeerName]["movingTime"] = speedLength
    dictionary[reindeerName]["restTime"] = restTime
    dictionary[reindeerName]["globalMoveTime"] = speedLength
    dictionary[reindeerName]["globalRestTime"] = restTime
    dictionary[reindeerName]["points"] = 0
    dictionary[reindeerName]["distance"] = 0

for i in range(raceTime):
    winningDistance = 0
    winningReindeers = []
    for name in names:
        if dictionary[name]["movingTime"] > 0:
            dictionary[name]["distance"] += dictionary[name]["speed"]
            dictionary[name]["movingTime"] -= 1
        else:
            if dictionary[name]["restTime"] > 1:
                dictionary[name]["restTime"] -= 1
            else:
                dictionary[name]["movingTime"] = dictionary[name]["globalMoveTime"]
                dictionary[name]["restTime"] = dictionary[name]["globalRestTime"]

        if dictionary[name]["distance"] > winningDistance:
            winningDistance = dictionary[name]["distance"]
            winningReindeers = [name]
        elif dictionary[name]["distance"] == winningDistance:
            winningReindeers.append(name)

    for winners in winningReindeers:
        dictionary[winners]["points"] += 1

winningPoints = max(dictionary[name]["points"] for name in names)
for name in names:
    print(name,dictionary[name]["points"])

print("Winning Points:",winningPoints)

