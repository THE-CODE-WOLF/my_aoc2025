import re
from os import remove

fileName = "Puzzles/day6"

with open(fileName, encoding="utf-8") as file:
    lines = [line.rstrip() for line in file]

#lines = ["123 328  51 64", "45 64  387 23", "6 98  215 314", "*   +   *   +"]

#print(lines[0][0])
#print(lines[1][0])
#print(lines[2][0])
#print(lines[3][0])
#print(lines[4][0])

total = 0

temp_nums = []

operations = re.findall("[+*]", lines[4])

for i in range(0, len(lines[0])):

    temp_nums.append(lines[0][i] + lines[1][i] + lines[2][i] + lines[3][i])

temp_nums.append(" ")

current_operation = 0

#print(temp_nums)

i = 0

for operation in operations:

    nums = []
    while re.findall("\d+", temp_nums[i]):
        nums.append(int(temp_nums[i]))
        i += 1
    i+= 1

    #print(nums, operation)

    if operation == "+":
        x = 0
        for num in nums:
            x += int(num)

        total += x
    else:
        x = 1
        for num in nums:
            x *= int(num)

        total += x

print(total)
