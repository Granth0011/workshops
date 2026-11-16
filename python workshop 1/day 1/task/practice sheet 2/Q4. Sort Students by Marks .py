marks=eval(input("Enter a dict of marks: "))
new_marks={}
for i in marks:
    new_marks[marks[i]]=i
print(new_marks)
new_marks=sorted(new_marks.items(),reverse=True)
for i in new_marks:
    print(i[1],i[0])