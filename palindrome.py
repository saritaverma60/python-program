#To find the string is palindrome or not
string=input("enter the string")
length=len(string)
rev=-1
mid=length//2
for a in range(0,mid):
    if string[a]==string[rev]:
       a+=1
       rev-=1
    else:
      print("not palindrom")
      break
else:
     print("palindrome")
