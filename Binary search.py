# To search key position with Binary Search method
list1=[2,45,67,69,89,99]
def bs(list1, key):
    l=0
    u=len(list1)-1
    found=False
    while l<=u and not found:
        mid=(l+u)//2
        if key==list1[mid]:
            found=True
        elif key>list1[mid]:
            l=mid+1
        else:
            u=mid-1
    if found==True:
        print("key is at position ",mid+1)
    else:
        print("key not found")
print(list1)
key=int(input("enter the value to  find"))
bs(list1,key)
              
        
