with open("input","r") as f:
    data = f.read().split("\n")

chars = list(data[0])

print(chars)
floor = 0

for char in chars:
    if char == "(":
        floor += 1
    if char == ")":
        floor -= 1

print(floor)