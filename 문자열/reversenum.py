a, b = input().split()
ans = a[::-1] > b[::-1]

if(ans):
    print(a)
else:
    print(b)