import time
try:
    n1=int(input("Enter a number : "))
    n2=int(input("Enter a number : "))
    sum=n1+n2
    print(sum)
    out=n1/n2
    print(out)
except ValueError:
    print("Please type only number in the Int form")
    time.sleep(1)
    print("Only number are accepted..")
    
except ZeroDivisionError:
    print("second number should not be zero.. ")
    








