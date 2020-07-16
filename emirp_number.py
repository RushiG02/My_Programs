#emirp number
def is_prime(n):
    if n<=1:
        return(False)
    if n<=3:
        return(True)
    if n%2==0 or n%3==0:
        return(False)
    i=5
    while(i*i<=n):
        if n%i==0 or n%(i+2)==0:
            return(False)
        i+=6
    return(True)

def is_emirp(n):
    if not(is_prime(n)):
        return(False)
    else:
        
        r=int(str(n)[::-1])
        if not(is_prime(r)):
            return(False)
    return(True)

print([n for n in range(1000) if is_emirp(n)])
