# Creating Class and objects
class Student:
    name = "saurabh"
    age = 20
    def study(self):
        print("Study 3 hours",self.name)
        self.sleep()
    def sleep(self):
        print("Sleep 1 hours",self.age)
        
obj = Student()
obj.study()


# private class = __name = "abc" , protected class = _name = "abc"

# Hybrid Inheritance of class
class A:
    def show(self):
        print("This is show method")
class B(A):
    pass
class C(A):
    pass
class D(B,C):
    pass

obj1 = C()
obj1.show()


# method overloading
def sum(a,b,c):
    print(a+b+c)

sum(10,20,30)
sum(10,20)


# method overwriting
class bird:
    def intro(self):
        print("There are many types of birds.")
    def flight(self):
        print("Most of the birds can fly but some can not.")
        
class sparrow(bird):
    def flight(self):
        print("I can fly.")

class ostrich(bird):
    def flight(self):
        print("I can not fly.")
        
obj = sparrow()
obj.flight()
obj.intro()

# Polymorphism with Inheritance

# Polymorphism lets us define methods in the child class that have the same name as the methods in the parent class.
# In inheritance, the child class inherits the methods from the parent class.
# However, it is possible to modify a method in a child class that it has inherited from the parent class. 
# This is particularly useful in cases where the method inherited from the parent class doesn't quite fit the child class. 
# In such cases, we re-implement the method in the child class. 
# This process of re-implementing a method in the child class is known as Method Overriding.

