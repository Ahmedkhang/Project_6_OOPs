class Dog():
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed
    def bark(self):
        print(f"{self.name} says Woof!")

Dog_1  = Dog("Buddy", "Golden Retriever")     
Dog_1.bark()   