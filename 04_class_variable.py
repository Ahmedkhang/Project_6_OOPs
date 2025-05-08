class Bank:
    bank_name = ''
    @classmethod
    def change_bank_name(cls,name):
        cls.bank_name = name
name1 = Bank()
name2= Bank()

name1.change_bank_name('UBL') 
name2.change_bank_name('Meezan Bank') 
print(name1.bank_name)
print(name2.bank_name)       

