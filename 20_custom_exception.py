class InvalidAgeError(Exception):
     pass
def check_age(age):
        
        if age < 18:
                raise InvalidAgeError('Age must be 18+')

        else:

            print('You are eligible')
age  =int(input('ENter your age: '))            
            

try:     
 check_age(age)
except InvalidAgeError as e:
     print('Invalid age Error!!' + '',(e))
      
      