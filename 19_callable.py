class Multiplier:
    def __init__(self,factor):
        self.factor = factor
    def __call__(self,value):
        result = self.factor * value
        return result
    
one = Multiplier(3)
print(callable(one))
print(one(7))

         