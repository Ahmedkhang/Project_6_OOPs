class Countdown:
    def __init__(self,num):
        self.num = num
    def __iter__(self):
        return self
    def __next__(self):
        if self.num > 0:
            self.num -= 1
            return self.num
        else:
            raise StopIteration
        
num = Countdown(10)
for n in num:
    print(n)        
            