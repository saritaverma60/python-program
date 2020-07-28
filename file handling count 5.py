#WAF to count the no of words whose 1st letter starts with p in a file...
def count():
    f1=open("news.txt","r")
    data=f1.readline()
    L=data.split(" ")
    print(L)
    count=0
    while data :
        for i in L:
            if i[0]=="p":
                count+=1
        data=f1.readline()
        L=data.split(" ")
        print(L)
    print("no of words whose 1st letter starts with p",count)
count()
