A = input()
B = input()
C = input()
calculation = str(eval(A + '*' + B + '*' + C))
arr = list(calculation)

for i in range(10):
    print(arr.count(str(i)))


