persons = ["nitish", "hajipur", "pankaj"]

for i in persons: # this for loop is like for(auto i: arr) in c++
    print(i)


for i in range(0, 8, 1): # this for loop is like for(i=0; i<8; i++) in c++. 
    print(i)

# the above can also written as 

for i in range(8): # 0 and 1 place can be empty because in for loops it is set default for start 0 and increament 1 or we can change them as our wish
    print(i)

for i in range(3):
    print(persons[i])

for i in range(10):
    print(i)
    if(i == 5):
        break
else: #this will execute when the for loop is successfully iterated from first to last
    print("completed")    


for i in range(10):
    if i == 5:
        continue
    print(i)