import numpy as np
import re

lights  = np.zeros((1000,1000), dtype=int)

with open("input","r") as f:
    data = f.read().split("\n")

for datapoint in data:

    splits = re.split("([0-9])", datapoint, maxsplit=1)
    command = splits[0]
    values = "".join([splits[1],splits[2]])
    part1, _, part2 = re.split(" ", values)
    x1, y1 = re.split(",", part1)
    x2, y2 = re.split(",", part2)
        
    x1 = int(x1)
    x2 = int(x2) + 1
    y1 = int(y1)
    y2 = int(y2) + 1

    if command == "toggle ":
        lights[x1:x2, y1:y2] += 2 
        
    if command == "turn off ":
        lights[x1:x2, y1:y2] -= 1
        lights[lights < 0] = 0
        
    if command == "turn on ":
        lights[x1:x2, y1:y2] += 1
    
print(np.sum(lights))
print(lights)
