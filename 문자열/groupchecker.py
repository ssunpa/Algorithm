n = int(input())
cnt = 0
for i in range(n):
    word = input()
    test = [word[0]]
    for j in range(1, len(word)):
        if(test[len(test)-1] == word[j]):
            continue
        else:
            test.append(word[j])
    if(len(set(test)) == len(test)):
        cnt += 1
print(cnt)
