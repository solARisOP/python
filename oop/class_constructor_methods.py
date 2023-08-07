class Employee:
    company = "microsoft" # this is a class attribute
    def __init__(self): # this is a constructor # self is a complusory argument taken by methods in class it refers to the object which is calling this particular method
        print("object has been created")

    def details(self):
        print(f'name is {self.name} and company is {self.company}') 

    @staticmethod # it makes the below method to not take the self argument
    def cost():
        print("No self argument required")    


nitish = Employee() 
ravi = Employee()
nitish.cost() # this gets converted to this -> # Employee.cost(nitish)
ravi.name = "ravi"
ravi.company = "apple" # this will get first prference and not the class attribute and this is called instance attribute
nitish.name = "nitish"
nitish.details() # for this we have not defined the company attribute so the class attribute company will take the preference

Employee.company = "google" # we can change the class attribute like this

nitish.details()
ravi.details()

# and yes we can make diff attributes for diff classes