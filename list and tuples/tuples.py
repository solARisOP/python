t = (1,2,3,4,5) # tuples 

p = () #-> empty tuple
p = (5) # -> wrong way to declare a single element tuple
p = (4,) # -> single element tuple
print(p)
print(t)
# t[0] = 45 # -> cannot do it, tuples are immutable

print(t[0])

print(t.count(1)) #-> count of int
print(t.index(5)) #-> at which index the number is located at