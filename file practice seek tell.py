f1= open("abc.txt","rb")
f1.seek(10)
print (f1.read(4))
print(f1.tell())
f1.seek(5,1)
print (f1.read(4))
print(f1.tell())
f1.seek(-5,2)
print(f1.tell())
print (f1.read(4))
f1.close()