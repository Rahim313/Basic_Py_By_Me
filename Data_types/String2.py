x="hello world"
print(len(x))


#just print single char

print(x[0])

print(x[0],x[4])

# range of the string

print(x[0:3])

print(x[1:4])

#only last char

print(x[-1])

# Search or find

print("wo" in x)

#find location

print(x.find('w'))

print(x.find('e'))

print(x.find('o',2,7))


#capital

print(x.capitalize())
print(x.upper())