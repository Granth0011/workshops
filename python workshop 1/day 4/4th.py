def f1():
    f2()
    print("in the f2 function")
def f2():
    f3()
    print("in the f3 function")
def f3():
    try:
        print(5/0)
    except ZeroDivisionError:
        print("division by zero is not possible")
    print(5//2)