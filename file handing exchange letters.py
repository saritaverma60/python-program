#wap to read the content of file and display 'I' in place of 'E' while displaying
#the content of file all other characters should appear as it is.
def change():
    filename=open("writer.txt","r")
    data=filename.read()
    for i in data:
        if i=='e':
            print('i',end='')
        else:
            print(i,end='')
    filename.close()
change()
            
            
            
            
