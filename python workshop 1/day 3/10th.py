arr=[2,4,7,9,11,13,15,21,33,37,45]
def bin(arr,first,last,tar):
    if first>last:
        return -1
    mid=(first+last)//2
    if tar==arr[mid]:
        return mid
    elif arr[mid]>tar:
        last=mid
    elif arr[mid]<tar:
        first=mid+1
    return bin(arr,first,last,tar)
print(bin(arr,0,len(arr),15))