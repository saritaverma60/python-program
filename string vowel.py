# 1. Write a program to count the no. of vowels in a string.
string=input("Enter the string : ")
count=0
for i in string :
    if i in ('a','e','i','o','u','A','E','I','O','U'):
        count+=1
print("count the no. of vowels in a string : ",count)        


