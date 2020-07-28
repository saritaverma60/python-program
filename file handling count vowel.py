def countvowel():
    filename=open("content.txt","r")
    data=filename.readlines()
    print(data)
    count=0
    n=len(data)
    for i in range(n) :
        if data[i][0] in ('a','e','i','o','u','A','E','I','O','U'):
            if data[i][-2] in ('a','e','i','o','u','A','E','I','O','U'):
                count+=1
                print(data)
   
    filename.close()
    print("No of lines are :",count)
countvowel()
