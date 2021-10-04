t = int(input())

for i in range(t):
    num1, num2 = map(int, input().split())
    print('Case #{}: {}'.format(i+1, num1+num2))