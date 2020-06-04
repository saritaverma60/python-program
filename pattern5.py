#print the hollow  piramid 
n=int(input("enter the range"))
for row in range(0,n):
    for col in range(0,n):
        if col==0 or row==(n-1) or row==col :
            print("*",end="")
        else:
            print(end="  ")
    print()         
