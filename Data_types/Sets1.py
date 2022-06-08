#defining set
#method 1

st1={3,4,5,9,6,100,100}
print(type(st1))
print(st1)

#Method 2

st2=set([23,'hello',96])
print(type(st2))
print(st2)

#Adding elements

st1.add("hello lnb")
print(st1)

#Adding multiple elements

st1.update([13,2,4,5,'Arkedian'])
print(st1)


# remove if elements not found raise an error
st1.remove(4)
print(st1)

#st1.remove('Ark')
#print(st1)


#discard
st1.discard(100)
print(st1)

st1.discard(90)
print(st1)


# Operations

st4={1,2,3,4,7,"Arkedian"}
st5={2,4,8,9,"Arkedian","ArkedianArked"}

print(st4 - st5)

print(st1.difference(st2))

print(st4 | st5)
print(st4 & st5)



