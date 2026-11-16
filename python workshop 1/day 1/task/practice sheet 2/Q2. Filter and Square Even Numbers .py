x=eval(input("Enter a list of numbers: "))
z=[i**2 for i in x if i%2==0]
print(z)