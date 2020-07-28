# MULTIPLE BINARY FILE
import os
import pickle
def write():
    with open("binaryfile.dat","wb") as f :
        while True :
            rollno=int(input("enter the roll no :"))
            name=input("enter th`e name :")
            per=float(input("enter the percentage :"))
            rec=[rollno,name,per]
            pickle.dump(rec,f)
            ch=input("more record (y/n) :")
            if ch=="n":
                    break
    f.close()
       
def read():
    f=open("binaryfile.dat","rb")
    print("roll no  name  per")
    try :
        while True :
            rec=pickle.load(f)
            print(rec)
    except EOFError :
        print ("done")
        f.close()

def append():
    with open("binaryfile.dat","ab") as f :
        while True :
            rollno=int(input("enter the roll no :"))
            name=input("enter th`e name :")
            per=float(input("enter the percentage :"))
            rec=[rollno,name,per]
            pickle.dump(rec,f)
            ch=input("more record (y/n) :")
            if ch=="n":
                    break
    f.close()

def update():
    with open("binaryfile.dat","rb+") as f:
        a=int(input("enter the roll no : "))
        found=0
        position=0
        try:
            while True and found==0:
                rec=pickle.load(f)
                if rec[0]==a:
                    f.seek(position)
                    rec[2]=float(input("enter the updated percentage :"))
                    pickle.dump(rec,f)
                    found=1
                else:
                    position=f.tell()
        except Exception :
            print("record not found ! ")

def delete():
    f1=open("binaryfile.dat","rb")
    f2=open("binary2.dat","wb")
    found=0
    a=int(input("enter the rollno to be deleted"))
    try:
        while True:
            rec=pickle.load(f1)
            if rec[0]==a:
                found=1
            else:
                pickle.dump(rec,f2)
    except EOFError:
        f1.close()
        f2.close()
    if found==0:
        print("record not found")
    else:
        os.remove("binaryfile.dat")
        os.rename("binary2.dat","binaryfile.dat")
           
   
    
         
while True :
    print("1-->write \n2-->read \n3-->update \n4-->append \n5-->delete \n6-->exit ")
    c=int(input("enter the choice : "))
    if c==1:
        write()
    elif c==2:
        read()
    elif c==3:
        update()
    elif c==6:
        break
    elif c==4:
        append()
    elif c==5:
        delete()
    else:
        print("wrong input")
    print("\n\n")    
        
