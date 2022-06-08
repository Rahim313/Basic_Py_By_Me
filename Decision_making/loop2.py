# nested loop

for i in range(1,5):
    for j in range(i):
        print(i,end=" ")
    print()
    
    
#Printing stars   
    
for i in range(1,5):
    for j in range(i):
        print("*",end=" ")
    print()
    
    
#loop controller

for letter in "lnbcore":
    if letter=="e" or letter=="b":
        continue # dont want to perform anything continue as it is
    print("heyyy")
    print("My current value is:",letter)
    
#using break to entire loop    
    
for letter in "lnbcore":
    if letter=="e" or letter=="b":
        break
    print("heyyy")
    print("My current value is:",letter)
    
    
#pass empty loops

for letter in "lnbcore":
    if letter=="l":
        pass
    else:
        print("hello",letter)
        
        
#for with else

for letter in "lnbcore":
    if letter=="e" or letter=="b":
        continue # dont want to perform anything continue as it is
    print("heyyy")
    print("My current value is:",letter)
else:
    print("i am else .. after for loop")
    