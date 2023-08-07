class Employee:
    def getme(self):
        print("this is employee")

    def chill(self):
        print("this is chill of employee")    

class Freelancer(Employee):
    def getme(self):
        print("this is freelancer")

    def chill(self):
        print("this is chill of freelancer")

class Programmer(Freelancer):
    
    def lexo(self):
        print("this is programmer")


p = Programmer()
p.getme()
