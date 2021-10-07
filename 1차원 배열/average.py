c = int(input())

for x in range(c):
    case = list(map(int, input().split()))
    sum = 0
    cnt = 0
    for y in case[1:]:
        sum += y
    average = sum/case[0]
    for z in case[1:]:
        if(z > average):
            cnt += 1
    result = cnt/case[0]*100
    print('%.3f%%'%(result))
