import re

fileName = "Puzzles/day1"

with open(fileName, encoding="utf-8") as file:
    lines = [line.rstrip() for line in file]

dial_num = 50
count = 0

test_lines = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82", "L1000"]

for line in lines:

    #print(line)

    direction = re.findall("[LR]", line)[0]
    amount = int(re.findall(r"\d+", line)[0])

    if direction == "L":
        amount *= -1

    start = dial_num
    end = dial_num + amount

    #print(direction, amount)

    if amount > 0:

        loops = (end // 100) - (start // 100)
    elif amount < 0:

        loops = ((start - 1) // 100) - ((end - 1) // 100)
    else:
        loops = 0

    count += loops

    dial_num = end % 100

print(count)
