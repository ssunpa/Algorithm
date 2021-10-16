alp = {2:['A','B','C'], 3:['D','E','F'], 4:['G','H','I'], 5: ['J','K','L'], 6:['M','N','O'], 7:['P','Q','R','S'], 8:['T','U','V'], 9:['W','X','Y','Z']}
sec = 0
num = list(input())
for i in num:
    for x, y in alp.items():
        if(i in y):
            sec += x+1

print(sec)
