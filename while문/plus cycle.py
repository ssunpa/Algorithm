n = int(input())
cnt = 0
oa, ob = n//10, n%10

while True:
    new = (ob*10) + ((oa+ob)%10)
    oa, ob = new//10, new%10
    cnt += 1
    if(new == n):
        break

print(cnt)
