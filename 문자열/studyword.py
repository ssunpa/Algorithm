word = input().upper()
test= set(word)
frequency = dict()

for i in test:
    frequency[i] = word.count(i)

maxnum = max(frequency.values())
maxalp = list()

for key, value in frequency.items():
    if(value == maxnum):
        maxalp.append(key)

if(len(maxalp) > 1):
    print('?')
else:
    print(maxalp[0])