import math

a, b, c = map(int, input().split())

if((c-b) == 0 or a/(c-b) < 0 ):
    print(-1)
elif(a/(c-b) == int(a/(c-b))):
    print(int(a/(c-b)+1))
else:
    print(math.ceil(a/(c-b)))

