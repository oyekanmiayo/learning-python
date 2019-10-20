phonebook = {}
phonebook[1] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)

phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
print(phonebook)

for name, number in phonebook.items():
    print("The phone number of %s is %d" %(name, number))

del phonebook["John"]
print(phonebook)

phonebook.pop("Jill")
print(phonebook)