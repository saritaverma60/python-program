#menu driven program for single record in binary file
import pickle
def write2():
    f=open("binaryfile1.dat","wb")
    rec=[]
    while True :
        rollno=int(input("enter the roll no :"))
        name=input("enter the name :")
        grade=input("enter")
        per=float(input("enter the percentage :"))
        r=[rollno,name,grade,per]
        rec.append(r)
        ch=input("more record (y/n) :")
        if ch=="n":
                break
    pickle.dump(rec,f)        
    f.close()

def read2():
    
    with open("binaryfile1.dat","rb") as f:
        try:
            while True:
                rec=pickle.load(f)
                print(rec)
                break
        except Exception as e:
            print(e)
    
def app():
    f=open("binaryfile1.dat","rb+")
    rec=pickle.load(f)
    while True :
        rollno=int(input("enter the roll no :"))
        name=input("enter the name :")
        grade=input("enter")
        per=float(input("enter the percentage :"))
        r=[rollno,name,grade,per]
        rec.append(r)
        ch=input("more record (y/n) :")
        if ch=="n":
            break
    f.seek(0)
    pickle.dump(rec,f)        
    f.close()

        
def update():
    with open("binaryfile1.dat","rb+") as f:
        rec=pickle.load(f)
        for i in rec:
           if i[3]>=90:
                i[2]='A'
           elif i[3]<90 and i[3]>=80:
                i[2]='B'
           else:
                i[2]='C'
        f.seek(0)
        pickle.dump(rec,f)
def dele():
    f=open("binaryfile1.dat","rb+")
    rec=pickle.load(f)
    r=[]
    found=0
    a=int(input("enter the rollno to be deleted"))
    for i in rec:
        if i[0]==a:
            found=1
        else:
            r.append(i)
    if found==0:
        print("record not found")
    else:
        f.seek(0)
        pickle.dump(r,f)
    f.close()
    
while True :
    print("1-->write \n2-->read \n3-->update\n4-->app\5-->delete 6---->exit")
    c=int(input("enter the choice : "))
    if c==1:
        write2()
    elif c==2:
        read2()
    elif c==3:
        update()
    elif c==4:
        app()
    elif c==5:
        dele()
    elif c==6:
        break
    else:
        print("wrong input")
    




    
        
        
