n = int(input())
cnt = 0

while True:
    if(n%5 != 0):
        n -=  3
        cnt += 1
        if(n % 5 == 0):
            cnt += n//5
            break
        elif(n == 0):
            break
        elif(n < 0):
            cnt = -1
            break
    else:
        cnt += n//5
        break
    
print(cnt)