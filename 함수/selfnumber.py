def d(n):
    selfnum = list()   
    for x in range(1, n+1):
        selfnum.append(x)
    for y in range(1, n+1):
        sum = 0
        for z in str(y):
            sum += int(z)
        sum += y
        if(int(sum) in selfnum):
            selfnum.remove(int(sum))
    
    for i in selfnum:
        print(i)
            
d(10000)