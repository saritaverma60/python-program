#print the hollow  piramid reverse form
n=int(input("enter the range"))
for row in range(0,n):
    for col in range(0,n):
        if row==0 or col==(n-1) or row==col :
            print("*",end="")
        else:
            print(end="  ")
    print()         
