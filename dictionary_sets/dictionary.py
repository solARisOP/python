dict = {
    "nitish" : "solaris", # keys : values
    "pankaj" : "godkiller",
    "abhishek" : "69_fps",
    "BJP" : {"RJD": "JDU"} # nested dictionary
}

print(dict["nitish"])
dict["abhishek"] = "69_FPS"
print(dict)
print(dict["BJP"]["RJD"]) # nested dictionary values access

# methods of dictionaries
print(list(dict.keys())) # Prints the keys of the dictionary
print(dict.values()) # Prints the keys of the dictionary 
print(dict.items()) # Prints the (key, value) for all contents of the dictionary 
print(dict)
updateDict = {
    "rgv": "Friend",
    "shrey": "Friend",
    "raushan": "Friend",
    "nitish": "A Dancer",
    1 : 2,
    "hajipur" : [9,7,6,6,3,23] 
}
dict.update(updateDict) # Updates the dictionary by adding key-value pairs from updateDict
print(dict)

print(dict.get("nitish")) # Prints value associated with key "harry"
print(dict["nitish"]) # Prints value associated with key "harry"

# The difference between .get and [] sytax in Dictionaries?
print(dict.get("nitish2")) # Returns None as harry2 is not present in the dictionary
print(dict["nitish2"]) # throws an error as harry2 is not present in the dictionary