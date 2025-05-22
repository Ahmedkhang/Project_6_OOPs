# This is an example of aggregation

class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def __str__(self):
        return f"Engine Horsepower: {self.horsepower}"
class Car:
    def __init__(self,name,model,engine):
        self.name = name
        self.model = model
        self.engine = engine
    def __str__(self):
        return f'my Car name is {self.name} and model is {self.model} and engine horsepower is {self.engine.horsepower}'
engine = Engine(200)
car = Car('Toyota','2021',engine)
print(car)  

#   This is an example of composition in Python, where a class (Car) contains an instance of another class (Engine) as an attribute.          
    
class Engine:
    def engine_start(self):
        print('ENgine Started')
class Car:
    def __init__(self):
        self.engine = Engine()
    def start(self):
        self.engine.engine_start()

car = Car()
car.start()                    