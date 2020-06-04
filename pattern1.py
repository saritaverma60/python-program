#print the pattern piramid
num= int(input("enter the rows"))
for i in range(num):
    for j in range(0, num-i-1):
        print(end=" ")
    for k in range(0,i+1):
        print("*", end=" ")
    print()    
    
