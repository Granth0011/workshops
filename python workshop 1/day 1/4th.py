# WAP to print all the numbers from 100 to 1000 which are prime and the sum of whose digits are also prime
def prime(a):
    x=True
    for j in range(2,a//2+1):
        if a%j==0:
            x=False
            break
    return x
for i in range(2,1000):
    if prime(i)==True:
        if i>9:
            x=sum(list(map(int,list(str(i)))))
            if prime(x)==True:
                x=sum(list(map(int,list(str(i)))))
                print(i)
                pass
            else:
                continue
        else:
            print(i)
            pass