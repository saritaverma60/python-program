def read():
    try:
        f1=open("test.txt",'r')
        data=f1.read()
        print(data)
        f1.close()
    except FileNotFoundError:
        print(" File not found ")
        
def filecopy():
    f1=open("test.txt",'r')
    f2=open("book.txt",'w')
    line=f1.readline()
    L=line.split(' ')
    print(L)
    while line:
        for i in L:
            if i in ("school","School","SCHOOL"):
                f2.write(line)
        line=f1.readline()
        L=line.split(' ')
    f1.close()
    f2.close()  


def printing():
    f1=open("test.txt",'r')
    L=f1.readlines()
    max1=len(L[0])
    for i in L:
        if max1<len(i):
            max1=len(i)
            line=i
    print("The maximum characters are :",max1)
    print("----------------The line is :----------------- \n ",line)


def count():
    f1=open("abc.txt",'r')
    count1=0
    L=f1.readlines()
    print(L)
    for i in L:
        n=len(i)
        count1+=n
    f1.close()
    
    f1=open("abc.txt",'r')
    count2=0
    data=f1.read()
    l=data.split('\n')
    print(l)
    for i in l:
        count2+=len(i)
    print("The no. of characters with  :",count1)
    print("The no. of characters without  :",count2)
    f1.close()


def choose():
    f1=open("sport.txt",'r')
    f2=open("atheletic.txt",'w')
    line=f1.readline()
    L=line.split("-")
    while line:
        if L[1].lower()=="athelete":
            f2.write(L[2]+"-"+L[1])
        line=f1.readline()
        L=line.split('-')
        
    print("---------------------DONE SUCCESSFULLY---------------------")
    f1.close()


def search():
    f1=open("record.txt",'r')
    line=f1.readline()
    L=line.split("-")
    print("-----------------------SEARCHED RECORD-----------------------")
    print("  NAME   OCCUPATION    AGE  ")
    while line:
        if int(L[2])>30:
            print(L[1] , "-" , L[3] , "-" , L[2])
        line=f1.readline()
        L=line.split("-")
    f1.close()

while True :

    print("-----------------------------: MENU DRIVE :--------------------------------")
    print("ch=1 : copy a line from test.txt from book.txt having school")
    print("ch=2 : print the longest line in test.txt ")
    print("ch=3 : count total no. of character with and without (backslash n) ")
    print("ch=4 : write a function to search the record of a person having age more than 30 ")
    print("ch=5 : copy the file sport.txt to atheletic.txt only those have event name atheletic ")
    print("ch=6 : read a file ")
    print("ch=7 :exit ")
    print("\n")
    ch=int(input("ENTER YOUR CHOICE :"))
    if ch==1:
        filecopy()
    elif ch==2:
        printing()
    elif ch==3:
        count()
    elif ch==4:
        search()
    elif ch==5:
        choose()
    elif ch==6:
        read()
    elif ch==7:
        print("Completed")
        break
    else:
        print("Wrong Input !!")
        
    
    
    



    
            


    
        

    

    
    
