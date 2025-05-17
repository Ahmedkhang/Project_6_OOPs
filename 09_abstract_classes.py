from abc import ABC, abstractmethod

class Shape(ABC): # abstract class can't be instantiated
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self,width,height):
         self.width = width
         self.height = height

    def area(self):
         return self.width * self.height 
       
rect_1  = Rectangle(3,2)
print(f'Area of rectangle: {rect_1.area()}')       