# creating tuple with homogeneous values

t1=(10,20,30,40)
print(t1)
print(type(t1))


# Creating tuple with hetrogeneous values

t2=(10,20,30,4,40,20)
print(t2)

# Operations can perform on tuple

#length
my_len=len(t1)
print(my_len)


# Search

print(23 in t1)
print(20 in t2)

# Count elements

c=t2.count(20)
print(c)


# Max or min from tuples

print(min(t2))
print(max(t2))


