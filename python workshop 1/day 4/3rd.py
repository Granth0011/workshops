try:
    a=(int(input("enter first number:")))
    b=(int(input("enter second number:")))
    print(f"{a} divided by {b} is {a/b}")
    arr=[1,2,3,4,5]
    for i in range(0,6):
        print(arr[i],end=" ")
except ValueError:
    print("please enter a valid number")
except ZeroDivisionError:
    print("division by zero is not possible")
except TypeError:
    print("please enter valid numbers")
except NameError:
    print("please enter valid numbers")
except KeyboardInterrupt:
    print("program interrupted")
except EOFError:
    print("program interrupted")

except IndexError:
    print("index out of range")
print("program completed")