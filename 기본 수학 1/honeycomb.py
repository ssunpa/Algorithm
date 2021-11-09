n = int(input())
cnt = 0
ans = 0
start = 1
while(True):
    if n in range(start, 6*ans+2):
        print(cnt+1)
        break
    else:
        start = 6*ans+2
        cnt += 1
        ans += cnt
