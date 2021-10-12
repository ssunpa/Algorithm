def d(n):
    diff = set()
    cnt = 0
    for i in range(1, n+1):
        diff.clear()
        if(i < 10):
            cnt += 1
        else:
            for j in range(len(str(i))):
                if(j+1 == len(str(i))):
                    continue
                else:
                    diff.add(int(str(i)[j]) - int(str(i)[j+1]))                      
            if(len(diff) == 1):
                cnt += 1
    print(cnt)

n = int(input())
d(n)