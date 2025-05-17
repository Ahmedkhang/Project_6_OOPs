class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display_name(self):
        print('Name : ',self.name)

    

class Teacher(Person):
    def __init__(self,name,subject):
        super().__init__(name)  
        
        self.subject = subject
    def display_subject(self):
        print('Subject : ',self.subject)          

person1 = Teacher('John','Physics')   
# print(person1.name)
person1.display_name()
person1.display_subject()         