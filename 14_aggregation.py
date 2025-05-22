class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Employee(Name: {self.name}, Age: {self.age})"
class Department:
    def __init__(self,name, location, employee):
        self.name = name
        self.location = location
        self.employee = employee
    def __str__(self):
        return f"Department(Name: {self.name}, Location: {self.location}, Employee: {self.employee})"
employee = Employee('Arsii',26)
# print(employee)
depart = Department('HR','North Karachi',employee)
print(depart)        
        
