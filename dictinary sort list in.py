#sort the list alphabetically in a dictionary 
dict1={ 2:["abc","pqr","xyz","aac"],1:["xxx","sss","aaa"]}
def d(dict1):
    print("print the  sorted value")
    for j, k in dict1.items() :
        sorted_dic={j: sorted(k)}
        print(sorted_dic)
d(dict1)        
