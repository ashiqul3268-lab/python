# Parameterized Constructor

# class info:
#     def Myinfo(self, name, age):
#         print(f"my name is {name}, my age is {age}")

# x = info()

# x.Myinfo("Ashiqul", 18) 
# [line 3-9 is method not constructor]

# class info:
#     # This is the special constructor method
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print(f"my name is {self.name}, my age is {self.age}")

# # Now, you pass the arguments directly when creating the object
# x = info("Ashiqul", 18)
# print(x.name)

# instance method 
class speed:
    def ronaldo(self,name):
        print(f"This is {name}")

y = speed()
y.ronaldo("Christiano")
# speed.ronaldo("Christiano")  #[in istance method ei niyom kah korbe na]

# class method
class messi:
    @classmethod
    def classMethod(cls,no):
        print(f"I am number {no}")

messi.classMethod(10)
z = messi()
z.classMethod(10)

# static method

class neymar:
    @staticmethod
    def staticmethod():
        print("This is neymar jr, everybody")

m = neymar()
m.staticmethod()
neymar.staticmethod()