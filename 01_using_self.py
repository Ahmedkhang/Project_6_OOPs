class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def details(self):
        print(f'Name : {self.name}\nMarks : {self.marks}')    

student_1  = Student('John', 90)
student_2  = Student('Jane', 95)
student_2.details()
student_1.details()
