class Product:
    
    def __init__(self,price):
        self._price = price

    @property
    def price(self):
        return self._price 
    @price.setter
    def price(self,price):
        self._price = price
    @price.deleter
    def price(self):
        print('Deleting....')
        del self._price
        
p1 =Product(21)
p1.price = 30

print(p1.price)   
del p1.price

# print(p1.del_price)