#4. WAP to swap the content with the next value which is divisible by 5.
#EXAMPLE : L=[3,25,13,6,35,8,14,45]
#EXPECTED OUTPUT---> L=[25,3,13,35,6,8,45,14]

L=[3,25,13,6,35,8,14,45]
print("List : ",L)
n=len(L)
i=0
while i<=n:
    if L[i]%5==0:
        L[i],L[i-1]=L[i-1],L[i]
        i=i+2
    else:
        i=i+1
print("Sorted List : ",L)
    
    
