# recursion check no is prime
def check(n, s):
    while s>=2:
        if n%s==0:
            print("not prime")
            return False
        else:
            return check(n,s-1)
    else:
         print("prime")
         return True
n=15
check(n,n-1)
