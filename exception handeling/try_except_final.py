a = int(input("input a number : "))

arr = [1,3,4,5]

try :
    print(arr[a])
except :
    print("wrong index")
finally :
    print("always executable")


