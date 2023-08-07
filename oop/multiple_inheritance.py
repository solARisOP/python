class Employee:
    def getme(self):
        print("this is employee")

    def chill(self):
        print("this is chill of employee")    

class Freelancer:
    def getme(self):
        print("this is freelancer")

    def chill(self):
        print("this is chill of freelancer")

class Programmer(Employee, Freelancer):
    
    def lexo(self):
        print("this is programmer")

p = Programmer()
p.getme() # employees getme will run coz its first inherited

