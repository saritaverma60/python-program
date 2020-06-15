# 2. Check whether string is palindrome or not.

#WAY 1
string=input("Enter the string : ")
str1=""
for i in string:
    str1=i+str1
print(str1)
if string == str1:
    print("String is palindrome ")
else:
    print("String is not palindrome ")

#WAY 2
string=input("Enter the string : ")
str1=""
n=len(string)
for i in range(n-1,-1,-1):
    str1+=string[i]
print(str1)
if string == str1:
    print("String is palindrome ")
else:
    print("String is not palindrome ")

#WAY 3
string=input("Enter the string : ")
str1=string[::-1]

print(str1)
if string == str1:
    print("String is palindrome ")
else:
    print("String is not palindrome ")

    



