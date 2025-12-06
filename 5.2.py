import re

fileName = "Puzzles/day5"

with open(fileName, encoding="utf-8") as file:
    lines = [line.rstrip() for line in file]

#lines = ["3-5", "10-14", "10-20", "12-18",  "1", "5", "8", "11", "17", "32"]

ranges = re.findall("\d+\-\d+", str(lines))

print(ranges)

#split_ranges = []

num_IDs = 0

mins = []
maxs = []

for arange in ranges:

    arange = arange.split("-")
    mins.append(int(arange[0]))
    maxs.append(int(arange[1]))

#mins = sorted(mins)
#print(mins, maxs)

sorted_ranges = sorted(zip(mins, maxs))
#print(sorted_ranges)
merged = [list(sorted_ranges[0])]
#print(merged)

for start, end in sorted_ranges:
    if start > merged[-1][1]:
        merged.append([start, end])
    else:
        merged[-1][1] = max(merged[-1][1], end)

for a, b in merged:
    num_IDs += b - a + 1

print(num_IDs)