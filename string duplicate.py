# 3. Remove duplicate characters in a string .

string=input("Enter the string : ")
str1=""
for i in string:
    if i not in str1:
        str1=i+str1
    
print(str1)        
