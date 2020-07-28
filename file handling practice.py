file=open('xyz.txt','r')
data=file.read()
l=data.split('\n')
print(l)
n=0
for i in l:
    n+=len(i)
print(n)
