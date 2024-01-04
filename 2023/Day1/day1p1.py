total = 0
num_adds = []
map = {"one":"1", "two":"2", "three":"3", "four":"4", "five":"5","six":"6", "seven":"7", "eight":"8", "nine":"9"}
with open("input.txt","r") as f:
    data = f.read().split("\n")
    for line in data:
        newline = line
        for key,val in map.items():
            newline = newline.replace(key,val)
        # print(line)
        # print(newline)
        nums = [int(s) for s in newline if s.isdigit()]
        # print(nums)
        to_add = nums[0]*10 + nums[-1]
        num_adds.append(to_add)
        # print("\n")
        total += to_add
    print(total)



### Sol 1

# total = 0
# with open("input.txt","r") as f:
#     data = f.read().split("\n")
#     for line in data:
#         nums = [int(s) for s in line if s.isdigit()]
#         total += (nums[0]*10 + nums[-1])
#     print(total)


import re

# get daily input
with open("input.txt","r") as f:
     input = f.read()


# part 1
result_part_1 = 0

# part 2
# dictionary for simpler string-to-int conversion
string_digits = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
}

result_part_2 = 0
numbers_add = []

for line in input.splitlines():
    # find all occurences of a number or written number in the string (even if overlapping or double)
    digits = re.findall("(?=([0-9]|one|two|three|four|five|six|seven|eight|nine))", line)
    new_digits = [string_digits[digit] for digit in digits]
    numbers_add.append(new_digits[0]*10 + new_digits[-1])
    # add only the first and last digit to the result
    result_part_2 += string_digits[digits[0]]*10 + string_digits[digits[-1]]


# print the results
print(f"Part 1: {result_part_1}")
print(f"Part 2: {result_part_2}")

