name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")

if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")

#is keyword matches instances while == matches values
x = [1,2,3]
y = [1,2,3]
print(x == y) # Prints out True
print(x is y) # Prints out False

#not inverts boolean
print(not False)