import math
def is_strong(n):
    t=n
    s=0
    while(t):
        r=t%10
        s+=math.factorial(r)
        t//=10
    if n==s:
        return('True')
    else:
        return('False')

print([n for n in range(50000) if is_strong(n)=='True'])
