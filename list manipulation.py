#2. Write a program to add 5 to odd values and 10 in even values of the list 'L'.
L=[]
L=eval(input("Enter the integer elements in the list :"))
n=len(L)
for i in range(n):
    if i%2==0:
        L[i]=L[i]+10
    else :
        L[i]=L[i]+5
print("The new list : ",L)
        
        
