#defining a list with homogeneous type

x1=[12,23,34,45,78]

#checking type

print(type(x1))
print(x1)

#creating a list with hetrogeneous type of data

x2=[12,23,45,78,'rahim',34]

# checking type 

print(x2)

# creating empy list
print("Below is empty list")
x3=[]
print(x3)
print("the above is empty list")


#operation in list 



# calculating length of list

length=len(x1)
print(length)
length1=len(x2)
print(length1)
length=len(x3)
print(length)

#They are mutable

#adding element using append

x1.append(100)
print(x1)


#adding element using insert

x1.insert(0,"Hi I am Arked")
print(x1)


#adding multiple values in the last of the list

x1.extend((0,77,"nice"))
print(x1)
x1.extend([10,2,31,45,23,'nice man'])
print(x1)

#removing element by position 

x1.pop()
print(x1)

x1.pop(0)
print(x1)

#removing by value
# removes the first apperance of the value in the list 

x1.remove(23)
print(x1)