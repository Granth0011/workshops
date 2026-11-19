def foo(n):
    if n == 0:
        return
    foo(n-1)
    print(n, end=" ")
    foo(n-1)

foo(4)