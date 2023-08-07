a = input("enter an integer between 5 and 9 : ")

if(a == "quit"):
    print("good")
elif(int(a)<5 or int(a)>9):
        raise ValueError("value should be between 5 and 9")

