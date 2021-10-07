case = int(input())
quiz = list()
score = 0
cnt = 0

for i in range(case):
    quiz.append(input()) 

for i in range(case):
    for j in quiz[i]:
        if(j == 'O'):
            cnt += 1
            score += cnt
        else:
            cnt = 0
    print(score)
    score, cnt = 0, 0
