#adding two list 
x1=[12,23,4,45,78]
x1.append(12)
x2=[12,23,45,3,'Hello world']

x3=x2+x2
print(x3)


# Indexing concept

#use
print(x1[3])

#slicing concept

s1=x1[0:3]
print(s1)

#print(x3[1::3])
#jumping elements

print(x3[0::2])

#clearing all elements

#x1.clear()
print(x1)

# counting number of elements


print(x3.count(12))

#sorting 
print(x1)
x1.sort()
print(x1)

#sum up all elements in list

print(sum(x1))

#max and min elements of list

print(max(x1))
print(min(x1))

# Nested List

x4=[2,"hiii",x1]
print(x4)

# Slicing

print(x4[1:3])