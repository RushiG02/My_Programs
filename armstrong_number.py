import math
def no_digit(n):
    d=0
    while(n):
        n//=10
        d+=1
    return(d)
def is_armstrong(n):
    d=no_digit(n)
    t=n
    s=0
    while(t):
        r=t%10
        s+=math.pow(r,d)
        t//=10


    if n==s:
        return('True')
    else:
        return('False')

a=[n for n in range(10000) if is_armstrong(n)=='True']

print(a)
