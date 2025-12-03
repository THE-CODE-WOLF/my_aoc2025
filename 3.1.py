
fileName = "Puzzles/day3"

with open(fileName, encoding="utf-8") as file:
    lines = [line.rstrip() for line in file]

#lines = ["987654321111111",
#         "811111111111119",
#         "234234234234278",
#         "818181911112111"]

joltage = 0

for line in lines:
    #print(line)
    length = len(line)
    line = list(line)
    #print(line)
    max_battery = 0

    for i, battery in enumerate(line):
        for y in range(i + 1, length):
            #print(battery + line[y])
            max_battery = max(max_battery, int(battery + line[y]))

    #print("max", max_battery)
    joltage += max_battery

print(joltage)

