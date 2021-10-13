c = int(input())

for x in range(c):
    r, s = input().split()
    for i in s:
        for j in range(int(r)):
            print(i, end='')
    print()