# recursion fabonicci series 
n=int(input("enter the no. of  elements "))
def fab(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fab(n-1)+fab(n-2)
for i in range(n):
    r=fab(i)
    print(r,end= ' , ')
