# count line start and end with vowels.
def python() :
    file=open("story.txt","r")
    line=file.readline()
    #print(line)
    count=0
    while line :
        #print( line)
        n=len(line.strip())
        print(line[n-1])
        if line[0] in ('a','e','i','o','u','A','E','I','O','U'):
            print(line[0])
            if line[n-1] in ('a','e','i','o','u','A','E','I','O','U') :
                #print(line[n-1])
                count+=1
                print("The line is :",line)
        line=file.readline()
    print("the no of lines are :",count)
    file.close()
python()    
        
        
    
