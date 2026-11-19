sentence = 'python makes coding enjoyable'
d={}
for i in set(sentence):
    if i in d.keys():
        d[i]=d[1]+1
    else:
        d[i]=1
