class Logger:
    def __init__(self,message):
        self.message = message
        print(f"Logger initialized with message: {self.message}")
    def __del__(self):
        print(f"Logger with message '{self.message}' is being deleted")    


a = Logger('Hello World')
# print(a.message)    
