# write a statement in python to open text file NEWS.TXT so that new
#content can be written
def write():
    file=open("news.txt","a")
    n=int(input("enter the no of lines :"))
    for i in range(1,n+1):
        data=eval(input("Enter content: "))
        file.write(data)
        file.write('\n')
    file.close()
    print("Done Successfully")
write()
