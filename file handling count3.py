#wap to read the content of file and count how many vowels in it.
def count():
    file=open("writer.txt","r")
    data=file.read()
    count=0
    for i in data:
        if i in ('a','e','i','o','u','A','E','I','O','U'):
            count+=1
    file.close()
    print("no. of vowels in the file :",count)
count()

    
