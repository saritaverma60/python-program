# fibonacci series using for loop-0 1 1 2 3 5 8.........n
n=int(input("enter the limit of series"))
first=0
second=1
print(first,second,end=" ")
third=first +second
for i in range(1,n):
    print(third,end=" ")
    first=second
    second=third
    third=first+second
