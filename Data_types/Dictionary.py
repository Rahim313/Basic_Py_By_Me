# Empty dictonary

from tokenize import Name


d1={}

# checking type
print(type(d1))

# creating new dict

d2={'Name':"Rahim","Company":"IBM","Contact":8983353631}

# Printing keys
print(d2.keys())

# printng values

print(d2.values())

# calling any single key

print(d2["Company"])

#adding elements in dict

d1[0]="Hello world"

print(d1)

d2['age']=24

print(d2)

#adding to dict

print(d1|d2)

#updating the value 

d1['age']=29
print (d1)
d2[100]="I am 100"
print(d1.keys())

# Deleting any key

del d1[0]

print(d1)

print(d2)

#Pop item from dict

value=d2.pop("age")
print("value associated with age is : "+ str(value))
print(d2)

#clear dic

#d2.clear()
print(d2)

#adding dict in another dict


d1["Arked"]=d2
print(d1)

print(d1['Arked'])
print(d1['Arked']['Name'])

