name = "John"
age = 23
print("%s is %d years old" %(name,age))

data = ("John", "Doe", 53.44)
format_string = "Hello %s %s, your current balance is $%s"
print(format_string % data)

aString = "Hello World!"
print(aString.index("o"))
print(aString.count("l"))
#prints between index 3 and 6
print(aString[3:7])
#prints element at index 0
print(aString[0])
#prints element from index 0 to index 6
print(aString[:6])
#prints from index 6 to the end
print(aString[6:])
#prints from the 3rd character from the end to the end
print(aString[-3:])
#prints from index 0 to end, and steps over 2 characters
print(aString[0::2])

#reverse a string
print(aString[::-1])
#uppercase
print(aString.upper())
#lowercase
print(aString.lower())
#does the string start with...
print(aString.startswith("Ayo"))
#does the strind end with...
print(aString.endswith("World!"))

#splits string
print(aString.split())
