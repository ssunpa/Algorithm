a, b = input().split()
ans = a[::-1] > b[::-1]

if(ans):
    print(a[::-1])
else:
    print(b[::-1])