with open("input","r") as f:
    data = f.read().split("\n")

directions = list(data[0])

x = 0
y = 0
locations = set([])

for d in directions:
    if d == "^":
        y += 1
    if d == "v":
        y -= 1
    if d == ">":
        x += 1
    if d == "<":
        x -= 1
    locations.add((x,y))

print(len(locations)+1)

