with open("input","r") as f:
    data = f.read().split("\n")

data = [int(nums) for nums in data[:-1]]

inc = 0

for i,val in enumerate(data):
    if i == len(data)-1:
        break
    if data[i+1] > val:
        inc += 1

print(inc)
