import copy
class Shape:
    def clone(self):
        return copy.deepcopy(self)
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius 
    def __str__(self):
        return f"circle with radius{self.radius}"
class Rectangle(Shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height 
    def __str__(self):
        return f"Rectangle with width{self.width} and of height{self.height}"
    
prototype=Circle(10)
prototype1=Rectangle(5,10)
print(prototype)
print(prototype1)
obj=prototype.clone()
obj1=prototype1.clone()
obj.radius=3
obj1.width=3
obj1.height=6
print(obj)
print(obj1)
