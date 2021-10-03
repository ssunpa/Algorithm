hour, minute = map(int, input().split())

totalM = hour*60 + minute
resultM = totalM - 45

if(resultM//60 < 0):
    print(resultM//60 + 24, resultM%60)
else:
    print(resultM//60, resultM%60)