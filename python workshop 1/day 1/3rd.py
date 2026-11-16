# write a program to find the sum of  first 10 natural number
a=0
for i in range(10+1):
    a+=i
print(f"sum of 10 natural number is {a}")

# write a program to print the multiplication table of a number taken a an input
n=int(input("enter the number"))
table=1
for i in range(1,n+1): 
    print(f"{n}*{i}={n*i}")

# WAP to print the factorial of a number:
n=int(input("enter the number for factorial"))
z=1
for i in range(n+1,1,-1):
    z=z*i
print(z)

# WAP to find one number raised to another 
n=int(input("enter the number"))
z=2
for i in range(3,n+1):
    z=z**i
print(z)