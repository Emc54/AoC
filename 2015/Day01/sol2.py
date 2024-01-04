with open("input","r") as f:
    data = f.read().split("\n")

chars = list(data[0])

print(chars)
floor = 0

for idx,char in enumerate(chars):
    if floor == -1:
        print(idx)
    if char == "(":
        floor += 1
    if char == ")":
        floor -= 1

print(floor)