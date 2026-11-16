names=eval(input("Enter a list of names: "))
z=[". ".join(i[0].upper() for i in name.split())+"." for name in names]
print(z)