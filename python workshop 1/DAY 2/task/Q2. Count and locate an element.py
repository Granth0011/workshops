value=eval(input())
target=int(input())
count=[]
for i in value:
    if i==target:
        count+=[i]
print(len(count),count)