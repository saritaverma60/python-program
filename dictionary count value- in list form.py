#Write a python program to count the number of items
# in a dictionary  value that is a list. 
D1={}
n=int(input("Enter the no. of enteries :"))
for i in range(n):
    key=eval(input("Enter the Key :"))
    value=eval(input("Enter the value : "))
    D1[key]=value
print("Dictionary :",D1)
L1=D1.values()
vcount=0
for i in L1:
    if type(i)==list:
        vcount+=1
print(" Values in the form of list in a dictionary ",vcount)
        
