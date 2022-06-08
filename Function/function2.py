#variable length arguments

def myfunction(*x):
    for i in x:
        print(i)
    print(type(x))
    
#call

myfunction(100,56,"hello")


# arguments in forms of dicts

def lnb(**learner):
    
    print("first name is",learner['fname'])
    print("Roll number is",learner["rollnum"])
    
#calling my function

lnb(fname="arked",rollnum="lnb001")


# return data from a function

def square(x,y):
    return(x**2,y**3)

# calling function

print(square(2,3))
print(square(4,5))


#function overloading is not possible in python

#lamda function

cube=lambda x: x**3
print(cube(7))


# recursion ---  calling function it self

def recursion(k):
    if k>0:
        result=k+recursion(k-1)
        print(result)
    else:
        result=0
    return result

#calling function

recursion(5)




