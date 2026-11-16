numbers=eval(input())
odd=[]
even=[]
for i in numbers:
    if i%2==0:
        even+=i
    else:
        odd+=i
print(f"""Expected even: {even}
Expected odd: {odd}
""")