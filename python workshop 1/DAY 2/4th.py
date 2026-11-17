s=[5,1,2,4,5,3,1,2]
x=set()
for i in s:
    if i in x:
        print(i)
        break
    x.add(i)