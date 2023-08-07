class Employee:
    company = "Bharat Gas"
    salary = 5600
    salarybonus = 400
    # totalSalary = 6100

    @property # this will make the bellow fuction act like an attribute rather than a method this is also called as getter
    def totalSalary(self):
        return self.salary + self.salarybonus

    @totalSalary.setter # it is a setter it is mainly used to change values of attributes
    def totalSalary(self, val):
        self.salarybonus = val - self.salary # we are decreasing the bonus here by useing the values

e = Employee()
print(e.totalSalary) # this will call the totalsalary method and print it (getter is called)
e.totalSalary = 5800 # this will change other attributes by taking 5800 as a value iyt is possible because of setter (setter is called)
print(e.salary)
print(e.salarybonus)