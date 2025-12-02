import re

fileName = "Puzzles/day2"

with open(fileName, encoding="utf-8") as file:
    text = file.readlines()

#text = ["11-22", "95-115", "998-1012", "1188511880-1188511890", "222220-222224", "1698522-1698528", "446443-446449", "38593856-38593862", "565653-565659", "824824821-824824827", "2121212118-2121212124"]

Ids = re.findall("\d+-\d+", str(text))

print(Ids)

invalid_count = 0

for Id in Ids:

    start = int(re.findall("\d+", Id)[0])
    end = int(re.findall("\d+", Id)[1])

    #print(start, end)

    for x in range(start, end + 1):

        match = re.match(r"^(\d+)\1$", str(x))
        if match:

            #print("invalid = " + str(match.group()))
            invalid_count += int(match.group())

print(invalid_count)






