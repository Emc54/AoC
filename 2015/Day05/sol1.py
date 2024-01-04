with open("input","r") as f:
    data = f.read().split("\n")

import re
regexp = re.compile(r"(.)\1")


nice_strings = 0
for string in data:

    vowels = 0
    # Check for 3 vowels
    for char in string:
        if char in ["a","e","i","o","u"]:
            vowels += 1
    if vowels < 3:
        continue
    
    # Check for double letter
    if not re.search(regexp,string):
        continue

    # Check for bad strings
    if re.findall(r"ab|cd|pq|xy",string):
        continue

    nice_strings+=1

print(nice_strings)