# 3. Display the sum of all values from the list which are ending with 3 .
L=[]
L=eval(input("Enter the elements of the list : "))
n=len(L)
Sum=0
for i in range(n):
    if L[i]%10==3:
        Sum=Sum+L[i]
print("Sum of values which are ending with 3 :", Sum)

