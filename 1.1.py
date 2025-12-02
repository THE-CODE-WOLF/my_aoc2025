import re

fileName = "Puzzles/day1"

with open(fileName, encoding="utf-8") as file:
    lines = [line.rstrip() for line in file]

test_lines = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82", "L1000"]

dial_num = 50
count = 0

for line in lines:

    direction = re.findall("[LR]", str(line))
    amount = re.findall("\d+", str(line))
    amount = int(amount[0])

    print(direction, amount)

    if direction[0] == "L":
        amount *= -1

    dial_num += amount

    dial_num %= 100

    print(dial_num)

    if dial_num == 0:
        count += 1
        print("+")

print(count)
