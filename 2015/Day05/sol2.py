with open("input","r") as f:
    data = f.read().split("\n")

import re
regexp = re.compile(r"(\w)\w\1")
regexp2 = re.compile(r"(..).*\1")


nice_strings = 0
for string in data:
    
    # Check for 'aba' pattern 
    if not re.search(regexp,string):
        continue

    # Check for repeat doubles
    if not re.findall(regexp2,string):
        continue

    nice_strings+=1

print(nice_strings)