# merge two dictionary
def merges():
    d1={1:10,2:100}
    d2={1:100,3:200}
    d3={**d2,**d1}
    print(d3)
    d2.update(d1)
    print(d1)
    print(d2)
merges()        
def mergeadd():
    # adding two value of same keys in 2 dictionary.
    d1={'a':100,'b':200,'c':300,'d':10}                       
    d2={'a':300,'b':200,'d':400,'k':100}
    d={}

    for i in d1:
        if i in d2:      
            d[i]=d1[i]+d2[i]
                
        else:
            d[i]=d1[i]
    for j in d2:
        if j not in d:
            d[j]=d2[j]
    print(d)
mergeadd()    




