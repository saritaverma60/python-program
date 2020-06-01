str=eval(input("enter the LIST"))
s=list(str)
l=len(str)
firstmax=s[0]
firstmin=s[0]
secmax=None
secmin=None
for i in range(1,l):
    if s[i]>firstmax:
      secmax=firstmax
      firstmax=s[i]
    elif secmax == None or s[i]>secmax:
       secmax = s[i]
    if s[i]<firstmin:
        secmin=firstmin
        firstmin=s[i]
    elif secmin==None or s[i]<secmin :
         secmin=s[i]

print("fmax",firstmax)
print("smax",secmax)
print("fmin",firstmin)
print("smin",secmin)
