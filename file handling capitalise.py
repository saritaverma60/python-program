def filecopy():
    f=open("xyz.txt",'r')
    f2=open("abc.txt",'w')
    data=f.read()
    n=len(data)
    for i in range(n) :
        if data[i-1]=='\n' or i==0 :
            s= data[i].upper()
            f2.write(s)
        else:
            f2.write(data[i])
    '''else:
        f2.write(data[i])'''
       
    f.close()
    f2.close()  
filecopy()
