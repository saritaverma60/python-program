try:
    print ("hello")
    n1=int(input("enter no"))
    n2=int(input("enter no"))
    c1=n1+n2
    print (c1)
    print(n1/n2)
except ValueError:
    print("no not a string")
except NameError:
    print("no not found")
except Exception as e:
    print("error is",e)
else:
    print("run smothly")
finally:
    print("good bye")
