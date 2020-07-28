#wap of function istoupcount() to read the content of file content.txt,to
#count and display the occurence of  'is,to,up'.
def istoupcount():
    file=open("content.txt","r")
    data=file.readline()
    L=data.split()
    count=0
    n=len(L)
    for i in range(n):
        if L[i] in ('is','up','to'):
            count+=1
    file.close()
    print("Count of is up and to  :",count)
istoupcount()
