#1. Write a program to get the smallest no. from the list .
L=[]
L=eval(input("Enter the elements in the list : "))
n=len(L)
Min=L[0]
for i in range(1,n):
    if Min>L[i]:
        Min=L[i]
print("The smallest no. from the list :",Min)
