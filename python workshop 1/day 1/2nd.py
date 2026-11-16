# # write a program to get the greatest of 2 numbers
# a=3
# b=2
# if a>b:
#     print("a is greatest")
# else:
#     print("b is greatest")

# # wrte a program to get the greatest of 3 numbaer
# a=int(input("enter 1st number : "))
# b=int(input("enter 2nd number : "))
# c=int(input("enter 3nd number : "))
# if a>b:
#     if a>c:
#         print("a is greatest")
#     else:
#         print("c is greatest")
# else:
#     if b>c:
#             print("b is greatest")
#     else:
#         print("c is greatest")

# single line condition use
a=int(input("enter 1st number : "))
b=int(input("enter 2nd number : "))
c=int(input("enter 3nd number : "))

max1=("a is greatest" if a>b and a>c else ("b is greatest" if b>c else "c is greatest"))
print(max1)  