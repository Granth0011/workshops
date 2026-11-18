def maxi(arr):
    if len(arr)==1:
        return arr[0]
    return arr[0] if arr[0]>maxi(arr[1:]) else maxi(arr[1:])
d=[1,2,23,3,4,5,88]
print(maxi(d))