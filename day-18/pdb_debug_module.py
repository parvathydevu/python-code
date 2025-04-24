import pdb

def divide(a,b):
    pdb.set_trace()  #Breakpoint
    res=a/b
    return res
def add(a,b):
    #result=a+b
    print("Hi")
    result=a+b

    return result

a=10
b=5
print("before divide:",a,b)
print("after divide:",divide(a,b))
print("after add:",add(a,b))

