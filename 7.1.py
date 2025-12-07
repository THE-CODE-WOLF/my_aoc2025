import re

fileName = "Puzzles/day7"

with open(fileName, encoding="utf-8") as file:
    lines = [line.rstrip() for line in file]

#print(lines)

#lines = [".......S.......",
#         "...............",
#         ".......^.......",
#         "...............",
#         "......^.^......",
#         "...............",
#         ".....^.^.^.....",
#         "...............",
#         "....^.^...^....",
#         "...............",
#         "...^.^...^.^...",
#         "...............",
#         "..^...^.....^..",
#         "...............",
#         ".^.^.^.^.^...^.",
#         "..............."]

total = 0

line_array = []
for line in lines:
    line_array.append(list(line))

for y, line in enumerate(line_array):

    for x, char in enumerate(line):
        if char == "S" or char == "|" and y < len(line_array) - 1:
            if line_array[y+1][x] == "^":
                line_array[y + 1][x + 1] = "|"
                line_array[y + 1][x - 1] = "|"
                total += 1
            else:
                line_array[y + 1][x] = "|"

for line in line_array:
    print(line)

print(total)


