import numpy as np 

with open("input","r") as f:
    data = f.read().split("\n")

total = 0

for gift in data:
    l, w, h = gift.split("x")
    l = int(l)
    w = int(w)
    h = int(h)

    sides = sorted([l,w,h])

    total += (sides[0]+sides[1])*2 + np.prod(sides)

print(total)