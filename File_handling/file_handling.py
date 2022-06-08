# Create a file

'''

file_name=input("Enter file name to crearte : ")
l=["AI is good \n","Hello i am data scientist \n","I am Rahim \n"]
f=open(file_name,'w') #write mode will create file always
f.write(" I am best data scientist \n")
f.writelines(l)
f.close()

'''
#read file   #seek function

f=open("My.txt",'r')
data=f.read()
print(data)
f.seek(0)
lineonly=f.readline() # read only first line
print(lineonly)
f.close()


# moving file in python

import shutil
# file name
sourc="My.txt"
destinatio="C:/users/sarfr/Ark/aaa.txt"
output=shutil.move(sourc,destinatio)
print(output)