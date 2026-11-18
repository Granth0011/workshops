# def rev(stri):
#     if len(stri)==1:
#         return stri[0]
#     return stri[-1] + rev(stri[:-1])
# stri="ambar"
# print(rev(stri))
def pal(stri):
    if len(stri)<=1:
        return "yessssss"
    if stri[0]==stri[-1]:
        return pal(stri[1:-1])
    else:
        return "nooooooo"
stri=input()
print(pal(stri))