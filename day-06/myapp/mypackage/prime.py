import __main__
def checkprime(n):  #prime .py is module(collection of function)
    for i in range(2,n):
        if (n%i==0):
            return False
    return True
    
def getHighestprime(m,n):
    for i in range(n,m-1,-1):
        if (checkprime(i)):
            return i
    return None #None keyword none values.

def getAllprime(m,n):
    count=0
    primeNumbers=[]
    for x in range(m, n+1):
        if (checkprime(x)):
            count+=1
            primeNumbers.append(x)
    return count, primeNumbers

if __name__=="__main__":  #constructor
    #test first function to checkprime()
    print("10->" , checkprime(10))
    print("11->" , checkprime(11))

    #test getHighestprime()
    print("100,200->", getHighestprime(100,200))
