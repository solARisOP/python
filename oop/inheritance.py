class Employee:
    def getme(self):
        print("this is employee")

    def chill(self):
        print("this is chill of employee")    

class Programmer(Employee):
    
    def getme(self):
        print("this is programmer")

p = Programmer()

p.getme() # programmers getme will be executed because that class has that function other wise parent class function would have been executed

p.chill() # employees chill will be executed because programmer does not have it
