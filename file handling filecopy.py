
def filecopy(file1,file2):
    f1=open(file1,'r')
    f2=open(file2,'w')
    line=f1.readline()
    while line!='':
        f2.write(line)
        line=f1.readline()
    f1.close()
    f2.close()  
  
'''def main():'''
file1=input("enter the file to read")
file2=input("enter the file to write")
filecopy(file1,file2)

    
