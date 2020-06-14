#sort a dictionary with predefine function and without predefine function.
dict1={ 1:"abc",2:"xyz",7:"sss",3:"www"}
print ("unsorted dictionary")
print(dict1)
def pd(dict1):
    #print the dictinary
    print("print the dictinary sorted in ascending")
    for k in sorted(dict1) : 
        print ((k, dict1[k]), end =" ")
    print()
    print("print the dictinary in descending")
    for k in sorted(dict1, reverse=True) : 
        print ((k, dict1[k]), end =" ")
    print()
pd(dict1)
def wpd(dict1):
    L=[]
    for i in dict1:
        L.append(i)
    print("List of the key :",L)
    for j in range(len(L)):
        for k in range(len(L)-j-1):
            if L[k]>L[k+1]:
                L[k],L[k+1]=L[k+1],L[k]
    print("Sorted key list : ",L)
    d={}
    for i in range(len(L)):
        key=L[i]
        d[key]=dict1[key]
    print("sorted value", d)
wpd(dict1)                   
                   
                   
    
        
