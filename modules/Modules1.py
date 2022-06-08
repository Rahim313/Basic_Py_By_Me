import time

#best way to use module
from time import sleep
print("Hello world..!")
time.sleep(3)
print("Hey guys  i am using time module..")
sleep(5)
print(time.ctime())  #current time
print("ok google")

#demo

count=0
while count<2:
    count=count+1
    print("hey")
    sleep(2)
    print("Arked")
  
import os  
for i in dir(os):
    if "sys" in i:
        print(i)
        
        

#import direct package from os 

import os
os.system('notepad')

# identify process

import subprocess,time
cmd=input("Enter any command :")
out=subprocess.getstatusoutput(cmd)
if out[0]==0:
    print("command found")
    time.sleep(1)
    print(out[1])
else:
    print("command not found")







            
        

    
   
    

