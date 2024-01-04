with open("input","r") as f:
    data = f.read().split("\n")

total = 0

for gift in data:
    l, w, h = gift.split("x")
    l = int(l)
    w = int(w)
    h = int(h)

    lw = l*w
    wh = w*h
    lh = l*h
    small_size = min([lw,wh,lh])

    total += 2*(lw + wh + lh) + small_size

print(total)