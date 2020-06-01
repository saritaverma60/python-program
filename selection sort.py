# selection sort
list1=(eval(input ("enter the list to be sorted")))
def selec(list1):
    for i in range(len(list1)-1):
        mini=i
        for j in range(i+1,len(list1)):
            if list1[j]<list1[mini]:
                mini=j
        list1[i],list1[mini]=list1[mini],list1[i]
        print(list1)
        print()
    print ("sored value is",list1)      
selec(list1)   
            
    
