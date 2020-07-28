#count a in the file.
def python() :
    file=open("story.txt","r")
    line=file.read()
    c=0
    for i in line.split():
        if i=='a':
            c+=1
    print(c)
 
python()    
        
