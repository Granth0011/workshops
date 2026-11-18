def sumi(arr):
    if len(arr)==1:
        return arr[0]
    return arr[0]+sumi(arr[1:])
arr=[1,2,3,4,5,6]
print(sumi(arr))