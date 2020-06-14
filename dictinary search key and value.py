# wap to search a key,value,item from a dictionary in different three ways .
D1={}
n=int(input("Enter the no. of enteries :"))
for i in range(n):
    key=eval(input("Enter the Key :"))
    value=eval(input("Enter the value : "))
    D1[key]=value
print("Dictionary :",D1)
def searchkey(D1):
    ksearch=eval(input("enter the key to be searched :"))
    for i in D1:
        if i==ksearch:
            return i
      
    else:
        return "not found"
x=searchkey(D1)
if x=="not found":
    print("key is",x)
else:
    print("key is ",x,"and its value is ",D1[x])
    
def searchvalue(D1):
    vsearch=eval(input("enter the value to be searched :"))
    L=D1.values()
    for i in L:
        if i==vsearch:
            return "found"
        
    else:
        return "not found"
y=searchvalue(D1)
if y=="not found":
    print("value is",y)
else:
    print("value is ",y)
    
def searchitems(D1):
    isearch=eval(input("enter the key to be searched :"))
    m=D1.items()
    for i,j in m:
        if j==isearch:
            return i,j
        

        else:
            print(i)
    else:
        return "not found"
z=searchitems(D1)
if z=="not found":
    print("item is",z)
else:
    print("item is ",z)

    
    
