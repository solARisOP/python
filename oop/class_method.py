class Employee:
    company = "Camel"
    salary = 100
    location = "Delhi"

    @classmethod # this is for changing class attributes value here cls means class, if we dont metion this decorater than cls will act as self and u know what happens when self is taken as argument, it changes the object's attribute not class's 
    def changeSalary(cls, sal):
        cls.salary = sal # we are changing class's attribute here not objects because class is passed as a reference which is been possinble because of the class method

    # def changeSalary(self, sal): 
        # self.__class__.salary = sal # this is also one of the ways for changing claas attributes value



e = Employee()
print(e.salary)
e.changeSalary(455) # this will pass class as a refrence because in the class it is defined as class method
print(e.salary)
print(Employee.salary)
