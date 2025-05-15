class Employee:
    def __init__(self,name,age,salary):
        self.name = name # Public variable
        self._age = age # Protected variable
        self.__salary = salary # Private variable

access  = Employee('John', 30, 50000)
print(access.name) # Public variable can be accessed directly
print(access._age) # Protected variable can be accessed directly
print(access._Employee__salary) # Private variable cannot be accessed directly, it can be accessed tgrough name mangling

# However, this is not recommended. It breaks the encapsulation principle and goes against the idea of private variables. It's better to use getter and setter methods to access or modify private variables:

