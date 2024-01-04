with open("input","r") as f:
    data = f.read().split("\n")

data = [int(nums) for nums in data[:-1]]

inc = 0

for i,val in enumerate(data):
    b = i+2
    c = i+3
    if b == len(data)-1:
        break
    sumA = val + data[i+1] + data[b]
    sumB = data[i+1] + data[b] + data[c]

    if sumB > sumA:
        inc += 1
print(inc)
