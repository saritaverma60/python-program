#recursion form palindrome or not
def pal(a,s,e):
       if (s==e):
            return True
       if (a[s]!=a[e]) :
           return False
       if (s<e+1):
           return pal(a, s+1,e-1)
       return True
        
a="raar"
e=len(a)
s=0
x=pal(a,0,e-1 )
if x== True:
    print("pa")
else:
    print("not")
        
    
