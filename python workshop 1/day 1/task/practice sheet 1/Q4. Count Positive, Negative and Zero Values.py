number=eval(input())
p=0
n=0
z=0
for i in number:
    if i>=0:
        if i>0:
            p+=1
        else:
            z+=1
    else:
        n+=1
print(f"""Positive : {p}
Negative: {n}
Zero:{z}""")