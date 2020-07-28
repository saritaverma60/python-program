import pickle
def fun():
    list1=[10,20,30,40,100]
    f=open("list1.dat","wb")
    pickle.dump(list1,f)
    print("list added")
    f.close()

def read():
    f=open("list1.dat","rb")
    try:
        while True:
            Rec=pickle.load(f)
            print(Rec)
    except Exception  as e:
        print("done", e)
        f.close()
fun()        
read()




    
    
    
