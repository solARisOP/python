class Employee:
    def __init__(self):
        print("created employee")
    def getme(self):
        print("this is employee")

    def chill(self):
        print("this is chill of employee")    

class Freelancer(Employee):
    def __init__(self):
        super().__init__()
        print("created freelancer")
    def getme(self):
        print("this is freelancer")

    def chill(self):
        print("this is chill of freelancer")

class Programmer(Freelancer):
    def __init__(self):
        super().__init__()
        print("created programmer")
    
    def getme(self):
        super().getme() # for calling parent class function of same name
        print("this is programmer")


p = Programmer()
