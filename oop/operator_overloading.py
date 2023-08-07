class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, num2): # it is already available in python we just have to define it
        print("Lets add")
        return self.num + num2.num

    def __mul__(self, num2): # same applies for this too
        print("Lets multiply")
        return self.num * num2.num
    
    def __str__(self):
        return f"Decimal Number: {self.num}"
    
    def __len__(self):
        return 1

n1 = Number(4)
n2 = Number(6)
sum = n1 + n2 # possible because of the __add__ operator which be have defined 
mul = n1 * n2 # possible because of the _mull__ operator which be have defined 
print(sum)
print(mul)
print(n1) # possible coz of str method
print(n2)

print(len(n1)) # possible coz of len methods


# these all method are in pyhton already, we just have to define it as our use, these are called dunder methods