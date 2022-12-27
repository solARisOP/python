c= "solaris"
d = ' nitish'
e = ' fff " ggg' # we can use double quotes inside by using single quotes in both end
f = ''' janua hammar RJD " lover ho '''
# print(c + d+e+f) #-> string Concatenate

name = "raobhaijr"

print(name[0:4]) # print string from 0 to 3 index excluding 4
print(name[:4]) # same as name[0:4]
print(name[0:]) # same as name[0:9]

print(name[-1]) # indexing from end of the string begins with -1

print(name[-4:-1])

print(name[0:9:2]) # skipping every 2 charracter
print(name[0::2]) # same as print(name[0:9:2])

name = "jia ho bihar ke lala jia tu hajaar sala tani nachi ke tani khai ke tani nachi khai sabke mann behelawa re bhaiya"

print(len(name)) # length of the string
print(name.endswith("bhaiya")) # -> returns true or false
print(name.count("j")) # -> counts characters
print(name.capitalize()) # -> capitalize first char of string
print(name.find("jia")) # -> returns first occurence of the word of letter in the string
print(name.replace("jia", "haji")) #-> replaces all occurences of the word with new word


name = name.replace("jia", "haji") # replaces and updates the original string
print(name)
name = "wakanda forever \nmultiverse \t"
print(name)