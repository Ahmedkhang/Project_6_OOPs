# class A:
#     def show(self):
#         print(' i am from class A')
# class B(A):
#     def show(self):
#         print(' i am from class B')
# class C(A):
#     def show(self):
#         print(' i am from class C')
# class D(B,C):
#     pass
# d = D()
# d.show()                               
def my_decorator(func):
    def wrapper():
        print("Before the function runs")
        func()
        print("After the function runs")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
