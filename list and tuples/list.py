n = [1,5,9,6,7,32,74,574,54,2,47] # -> list creation
print(n)
n[0] = 90
print(n)

print(n[4])

a = ["nitish", 2, True, 9.4] #-> list with diff type of values
print(a)

print(n[0: 4])
print(n[-4:])

n.sort() # sorts the list
print(n)
n.reverse() # reverses the list
print(n)
n.append(45) # adds 45 at the end of the list 
print(n)
n.insert(2, 544) # inserts 544 at index 2
print(n)
n.pop(2) # removes element at index 2
print(n)
n.remove(5) # removes 5 from the list
print(n) 
