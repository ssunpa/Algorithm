n = int(input())
original = list(map(int, input().split()))
m = max(original)
sum = 0
for i in range(n):
    sum += original[i]/m*100

print(sum/n)