arr = []
for i in range(10):
    arr.append(int(input())%42)

cnt = set(arr)
print(len(cnt))
