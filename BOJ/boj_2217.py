# 2217. 로프

n = int(input())
weights = []

for i in range(n):
    weights.append(int(input()))

weights.sort()

max = 0
count = 1
for i in range(n-1, -1, -1):
    maxWeight = count * weights[i]
    if maxWeight > max:
        max = maxWeight
    
    count += 1

print(max)