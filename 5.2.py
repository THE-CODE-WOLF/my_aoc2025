import re

fileName = "Puzzles/day5"

with open(fileName, encoding="utf-8") as file:
    lines = [line.rstrip() for line in file]

#lines = ["3-5", "10-14", "16-20", "12-18", "1", "5", "8", "11", "17", "32"]

ranges = re.findall("\d+\-\d+", str(lines))

print(ranges)
