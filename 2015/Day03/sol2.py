with open("input","r") as f:
    data = f.read().split("\n")

directions = list(data[0])
s_directions = directions[::2]
rs_directions = directions[1::2]

x = 0
y = 0
locations = set([(x,y)])

for d in s_directions:
    if d == "^":
        y += 1
    if d == "v":
        y -= 1
    if d == ">":
        x += 1
    if d == "<":
        x -= 1
    locations.add((x,y))

x = 0
y = 0
for d in rs_directions:
    if d == "^":
        y += 1
    if d == "v":
        y -= 1
    if d == ">":
        x += 1
    if d == "<":
        x -= 1
    locations.add((x,y))

print(len(locations))

