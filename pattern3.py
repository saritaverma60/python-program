#print the pattern piramid both upper and lower with single for loop
rows= int(input("enter the rows"))
for i in range(rows):
    print(" "*(rows-1-i)+"*"*(i+1))
for j in range(rows-1,0,-1):
    print(" "*(rows-j)+"*"*(j))
