# Recursion Factorial of number
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
n=int(input("Enter the no. :"))
R=fact(n)
print("FACTORIAL of ",n," is ",R)
