#1-1/2+1/3-1/4
def new(n,sums,i=2):
    if i>n:
        return sums
    else:
        if i%2!=0:
            sums=sums-1/i
            return(new(n,sums,i+1))
        else:
            sums=sums+1/i
            return (new(n,sums,i+1))
try:
    n=int(input("enter"))
    result=new(n,1)
except Exception :
    print("error")
else:
    if n<=0:
        raise Exception("error not 0 or negative number")
    print(result)
finally:
    print("end")

