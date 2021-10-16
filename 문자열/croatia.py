word = input()
croatia = ['c=','c-','dz=','d-','lj','nj','s=','z=']
cnt = 0
for i in croatia: 
    if(i in word):
        cnt += word.count(i)
        word = word.replace(i, ' ')
        
print(cnt + len(word.replace(' ','')))



