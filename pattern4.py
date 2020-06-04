#print the hollow  piramid 

for row in range(7):
    for col in range(7):
        if row+col==3 or col-row==3 or row-col==3 or row+col==9:
            print("*",end=" ")
        else:
            print(end=" ")
    print()         
