#wap to read the content of file and display how many upper case characters
# and digits are present.
def count():
    filename=open("writer.txt","r")
    countU=0
    countD=0
    data=filename.read()
    for i in data:
        if i.isupper():
            countU+=1
        elif i.isdigit():
            countD+=1
    filename.close()
    print("no. of upper case characters : ",countU)
    print("No. of digits :" ,countD)
count()
    
