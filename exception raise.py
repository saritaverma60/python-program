def table():
        try:
            n=int(input("input value"))
        except ValueError:
                print("it is not a string")
        except Exception as e:
                 print(e)
        else:
            if n<15:
                raise Exception("no. should greater than 15")
        for i in range(1,5):
              print(n*i)
              
table()              
                
                      
