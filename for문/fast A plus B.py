import sys

t = int(input())
for i in range(t):
        num1, num2 = map(int, sys.stdin.readline().split())
        print(num1 + num2)