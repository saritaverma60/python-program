# linear search to search the element and print it's position.
def linear(list1,key):
    L=len(list1)
    index=[]
    flag=0
    for i in range(0,L):
        if list1[i]==key:
            flag=1
            index.append(i)
    if flag==1:
        return index
    else:
        return "not found"
    
list1=[]
list1=eval(input("Enter the elements :"))
key=int(input("Enter the element to be searched :"))
x=linear(list1,key)
print(list1)
if x=="not found":
    print("Element",key,"is not in the list")
else:
    print("Element",key,"is found . It is on",x,"position.")
