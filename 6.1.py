import re

fileName = "Puzzles/day6"

with open(fileName, encoding="utf-8") as file:
    lines = [line.rstrip() for line in file]

#lines = ["123 328  51 64", "45 64  387 23", "6 98  215 314", "*   +   *   +"]

print(lines)

total = 0

top_row = re.findall("\d+", lines[0])
middle_row = re.findall("\d+", lines[1])
lower_row = re.findall("\d+", lines[2])
bottom_row = re.findall("\d+", lines[3])
operations = re.findall("[+*]", lines[4])

print(top_row)
print(middle_row)
print(lower_row)
print(bottom_row)
print(operations)

for i in range(0, len(operations)):
    print(operations[i])
    if operations[i] == "+":
        total += int(top_row[i]) + int(middle_row[i]) + int(lower_row[i]) + int(bottom_row[i])
    else:
        total += int(top_row[i]) * int(middle_row[i]) * int(lower_row[i]) * int(bottom_row[i])

print(total)