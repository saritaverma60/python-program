# bubble sorting

def sort(list1):
    n=len(list1)
    print("Original List ", list1)
    for i in range(n):
        for j in range (n-i-1):
            if list1[j]>list1[j+1]:
                list1[j],list1[j+1]=list1[j+1],list1[j]
            print(list1)
        print()
    return list1
list1=[]
list1=eval(input("Enter the Elements of the List: "))
X=sort(list1)
print("Sorted List", X)

   
