#write a statement in python to open text file NEWS.TXT so that existing
#content can be read
def read():
    file=open("news.txt","r")
    data=file.read()
    print(data)
    file.close()
read()
