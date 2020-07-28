# MENU DRIVE PROGRAM to search a roll no in text file
def student_record():
    print("------------------ Enter Student Details : -------------------------")
    rollno=int(input("Enter the Roll No : "))
    name=input("Enter the Name : ")
    address=input("Enter Address : ")
    file1=open("student.txt",'a+')
    file1.write(str(rollno)+' , '+name+' , '+address+'\n')
    file1.flush()
    ch=input(" Do you want to add more records ? (y/n) : ")
    if ch=='y' or ch=='Y':
        student_record()
def read_data():
    try:
        file1=open("nandini.txt",'r')
        print("---------------- Students Information ----------------------")
        data=file1.read()
        print(data)
    except FileNotFoundError as e:
            print(e)
def search_student():
    roll_no=int(input("enter the searched roll no : "))
    file1=open("student.txt",'r')
    data=file1.readline()
    row=data.split(',')
    flag=0
    while data:
        if int(row[0])==roll_no:
            flag+=1
            print("-----------Searched File-------------")
            print(data)
            break
        data=file1.readline()
        row=data.split(',')
    if flag==0:
        print(" File not found " )
    else:
        print(" File is Found ")
        ch=input(" Do you want to search more files ? (y/n) ")
        if ch=='y' or ch=='Y':
            search_student()
    file1.close()
print("--------------------------------MENU DRIVE---------------------------------")
print("c=1   :- add a new student record \nc=2   :- display students details")
print("c=3   :- search student on the basis of roll no.")
print("\n")
c=int(input("Enter your choice to follow :"))
print('\n')
if c==1:
    student_record()
elif c==2:
    read_data()
elif c==3:
    search_student()
        
    
    
    
    
    
    
    
