def foo(n):
  if n<=0:
    return
  print(n,end=" ")
  foo(n-2)
  print(n-1,end=" ")
  foo(n-1)
foo(3)