# fibonacci series using while loop-0 1 1 2 3 5 8.........n
n=int(input("enter the end number of series"))
first=0
second=1
print(first,second,end=" ")
third=first+second
while third<n:
    third=first+second
    if third<=n:
        print(third,end=" ")
        first=second
        second=third
    
