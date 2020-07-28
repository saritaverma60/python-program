# search a record in text file
import os
def search(filename):
    with open(filename) as f:
        r=(input("enter record"))
        f=0
        line=f.readline()
        for i in line.split():
              if i==r:
                f=1
                break
        if f==1:
              print("not found")
        else:
              print("not found")
def main():
    filename=input("enter")
    search(filename)
main()    
    
              
