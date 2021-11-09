X = int(input())
x, y = 1, 1
cnt = 0
k = 1

while True:
    if(cnt%2 == 0):
        for i in range(cnt):        
            if(k == X):
                break
            k += 1
            x -= 1
            y += 1           
    elif(cnt%2 != 0):
        for i in range(cnt):        
            if(k == X):
                break
            k += 1
            x += 1
            y -= 1            
    if(k == X):
            break
    k += 1        
    if(x == 1):        
        y += 1
    elif(y == 1):
        x += 1
    cnt += 1

print('{}/{}'.format(x, y))