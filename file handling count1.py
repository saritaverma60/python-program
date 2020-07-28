# wap to read the content of file and count how many times letter 'a' comes in file.
def file():
    filename=open("writer.txt","r")
    data=filename.read()
    count=0
    for i in data:
        if i=='a' :
            count+=1
    print("No. of times 'a' comes :",count)
    filename.close()
file()
