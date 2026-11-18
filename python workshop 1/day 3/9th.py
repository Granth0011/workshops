def rev(stri):
    if len(stri)==1:
        return stri[0]
    return stri[-1] + rev(stri[:-1])
stri="ambar"
print(rev(stri))