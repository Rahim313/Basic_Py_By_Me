import time
import sys


i=10
try:
    i=i+"a"
except Exception as e:
    print("Unexpected error..",e.__class__)
    
    
#  try with else

try:
    num=int(input("Enter number : "))
    assert num % 2 == 0
except:
    print("Not an even number ..")
else:
    result=1/num
    print(result)
    

# try with finally

try:
    data=input("Enter data : ")
    print("Hello ",data)
except:
    print("I am error check  the code .")
finally:  #finally run every timee
    print("I am always going to run myself..")


    