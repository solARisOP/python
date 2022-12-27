mydict = {
    "pankha" : "fan",
    "kitaab" : "book",
    "pani"   : "water"
}

print(mydict.keys())

a = input("Enter the word from above keys : ")

# print(mydict[a])
print(mydict.get(a)) # this doesnot give error if wrong values are entered
