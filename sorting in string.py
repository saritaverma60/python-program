#string1=green-red-yellow-black-white
#string2=black-green-red-white-yellow
def sort(string1):
    print("Original string:", string1)
    L=[]
    L=string1.split("-")
    n=len(L)
    print("string1 to list", L)
    for i in range(n-1):
        for j in range(n-i-1):
            if L[j]>L[j+1]:
                L[j],L[j+1]=L[j+1],L[j]
    hyphen="-"
    string2=hyphen.join(L)
    return string2
    
    
string1="green-red-yellow-black-white"
X=sort(string1)
print("sorted string :",X)



