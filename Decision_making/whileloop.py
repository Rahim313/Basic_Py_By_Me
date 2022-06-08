#demo 1 
count=0
while count<3:
    count=count+1
    print("hello lnb")
    
#demo2
count=0
while count<3:count=count+1;print("hi lnb")


#demo 3 a list with while

lnb=[1,3,5,6]
while lnb:
    print(lnb.pop())
    print(lnb)
    
    
#loop controllers
i=0
a="hellolnb"
while i<len(a):
    if a[i]=="o" or a[i]=="b":
        i=i+1
        continue #break #pass can be used
    print("current letter is:",a[i])
    i+=1


#break statement

i=0
while i<4:
    i+=1
    print(i)
    break