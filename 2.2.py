import re


fileName = "Puzzles/day2"

with open(fileName, encoding="utf-8") as file:
    text = file.readlines()

#text = ["11-22", "95-115", "998-1012", "1188511880-1188511890", "222220-222224", "1698522-1698528", "446443-446449", "38593856-38593862", "565653-565659", "824824821-824824827", "2121212118-2121212124"]
#text = ["11-22", "100-200"]

Ids = re.findall("\d+-\d+", str(text))

print(Ids)

invalid_count = 0

for Id in Ids:
    start = int(re.findall("\d+", Id)[0])
    end = int(re.findall("\d+", Id)[1])
    print("Id", start, end)

    for x in range(start, end + 1):
        num_string = str(x)
        length = len(num_string)
        #print(length, num_string)

        if length == 2:
            a = int(num_string[0])
            b = int(num_string[1])
            if a == b:
                print("invalid " + num_string)
                invalid_count += int(num_string)

        for divisor in range(1, length - 1):
            #print(length % divisor == 0)
            #print(divisor)
            invalid = 0

            if length % divisor == 0:
                substring = num_string[:divisor]
                #print(substring, divisor)
                test_string = substring

                for i in range(int(length / divisor)):
                    test_string = test_string + substring
                    #print(test_string)

                    if test_string == num_string:
                        invalid = 1
                        print("invalid " + test_string)
                        invalid_count += int(test_string)
                        break

            if invalid:
                break


print(invalid_count)





#print(invalid_count)