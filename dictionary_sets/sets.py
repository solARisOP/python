n = {5, 90, 3, 54, 12, 25} # -> set
print(type(n))
print(n)

a = {} # -> this is an empty dictionary not an empty set
print(a)
print(type(a))
a = set() # -> empty set
print(type(a))

a.add(34)
a.add(4)
a.add(5)
a.add(5) # set doesnot contain duplicate values

print(a)
# a set cannot contain dictionary or list because they are unhasable meaning they can get changed in further, but sets values are immutable we cannot change a value that is present in the set

print(len(a))

a.remove(5) # -> removes 5 from the set
print(a)

print(a.pop()) # -> pops a random value and returns it
print(a)