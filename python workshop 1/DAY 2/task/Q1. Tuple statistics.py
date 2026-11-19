def tuple_report(numbers):
    z={}
    z["max"]=max(numbers)
    z["len"]=len(numbers)
    z["min"]=min(numbers)
    z["sum"]=sum(numbers)
    return z
numbers=eval(input())
print(tuple_report(numbers))
