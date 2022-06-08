# Storage concept of tuple

t1=(10,20,30,4,40,20,65)

print(t1)


#First element

print(t1[0])

#range print

print(t1[0:2])


#Jumping values

print(t1[0::4])

#Print last element only
print(t1[-1])

#Tuple inside tuple

t2=("Hello",23,t1)
print(t2)

#last elemet of t2
print(t2[-1])
print(t2[-1][0])

print(t2[-1][-1])



#Integration with for loop

tx=("lnb")
for i in range(2):
    tx=(tx,)
    print(tx)
    
