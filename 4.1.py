fileName = "Puzzles/day4"

with open(fileName, encoding="utf-8") as file:
    lines = [line.rstrip() for line in file]

#lines = ["..@@.@@@@.",
#         "@@@.@.@.@@",
#         "@@@@@.@.@@",
#         "@.@@@@..@.",
#         "@@.@@@@.@@",
#         ".@@@@@@@.@",
#         ".@.@.@.@@@",
#         "@.@@@.@@@@",
#         ".@@@@@@@@.",
#         "@.@.@@@.@."]

#lines = ["@......",
#         "@@.....",
#         "@......"]

#print(lines)

length = len(lines)

line_length = len(lines[0])

accessible = 0


for line_number, line in enumerate(lines):
    for num, item in enumerate(line):
        #print(line_number, item)
        if item == "@":
            num_around = 0
            #right
            if num < line_length - 1:
                if line[num+1] == "@":
                    num_around += 1
            #left
            if num > 0:
                if line[num-1] == "@":
                    num_around += 1
            #up
            if line_number > 0:
                if lines[line_number - 1][num] == "@":
                    num_around += 1
            #down
            if line_number < length - 1:
                if lines[line_number + 1][num] == "@":
                    num_around += 1
            # upper right
            if num < line_length - 1 and line_number > 0:
                if lines[line_number - 1][num + 1] == "@":
                    num_around += 1
            # upper left
            if num > 0 and line_number > 0:
                if lines[line_number - 1][num - 1] == "@":
                    num_around += 1
            # lower right
            if num < line_length - 1 and line_number < length - 1:
                if  lines[line_number + 1][num + 1] == "@":
                    num_around += 1
            # lower left
            if num > 0 and line_number < length - 1:
                if lines[line_number + 1][num - 1] == "@":
                    num_around += 1
            #print("num around", num_around)
            if num_around < 4:
                accessible += 1



print(accessible)