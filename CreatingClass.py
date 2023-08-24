#creating class method1
# class Student:
#     pass
# # s = Student() 

# #creating class method2
# class Student1:
#     def __init__(self): #Special function it calls itself
#         print("I m init() method")
# # s = Student1()

#creating class method3
class Student2:
    def __init__(self,name): #Special function it calls itself
        self.name=name
    def display(self):
        print("My name is:",self.name)
s = Student2("Suprika")
s.display()

