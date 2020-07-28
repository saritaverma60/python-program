#wap to read the content of file and count how many vowels in it.
def count():
    file=open("xyz.txt","r")
    data=file.readlines()
    count=0
    
    for i in data:
        n=len(i.strip())
        
        if i[0] in ('a','e','i','o','u','A','E','I','O','U'):
            if i[n-1] in ('a','e','i','o','u','A','E','I','O','U'):
                count+=1
    file.close()
    print("no. of vowels in the file :",count)
count()
