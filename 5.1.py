import re

fileName = "Puzzles/day5"

with open(fileName, encoding="utf-8") as file:
    lines = [line.rstrip() for line in file]

#lines = ["3-5", "10-14", "16-20", "12-18", "1", "5", "8", "11", "17", "32"]

ranges = re.findall("\d+\-\d+", str(lines))

#print(ranges)

nums = []

num_fresh = 0

for number in lines:
    if not ranges.__contains__(number) and number != "":
        nums.append(int(number))

#print(nums)

for number in nums:
    for x in ranges:
        split = x.split("-")
        if int(split[0]) <= number <= int(split[1]):
            #print(number)
            num_fresh += 1
            break

print(num_fresh)