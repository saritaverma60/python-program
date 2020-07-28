#Write a function countae() in python to read lines from text file writer.txt
#and display those lines which are starting either with A or starting with E.
def countae():
    filename=open("writer.txt","r")
    data=filename.readline()
    while data:
        if data[0]=='A' or data[0]=='E':
            print(data)
        data=filename.readline()
    filename.close()
countae()
