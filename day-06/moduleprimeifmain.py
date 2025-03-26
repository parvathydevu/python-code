def checkprime(n):
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
    return count, primeNumbers  #return two objects  it becomes tuple

'''if __name__=="__main__":  #constructor''' #without main function we can execute but....disadv
    #test first function to checkprime()
    
print("10->" , checkprime(10))
print("11->" , checkprime(11))

    #test getHighestprime()
print("100,200->", getHighestprime(100,200))

    #test getAllprime()
print("100,200->", getAllprime(100,200))  #when we import new project and import this prime into that new project.py , without if__main__ the new project code willnot excute

#Notes:without if __name__=="__main__":  #constructor'
''' importing modules will cause  the module to be executed where it is imported
when running directory prime.py __name__=="main" 
when i run new project (included main function in prime.py)- that new projet will execute succesfully and inside that the first python codepippython -m venv myenv will run correctly.'''