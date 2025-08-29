from abc import ABC, abstractmethod
import math

class shape(ABC):
    def area(self):
        pass

class reactangle(shape):
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    
    def area(self):
        return self.length*self.breadth
    
class circle(shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return math.pi*self.radius**2
    
r = reactangle(24,45)
c = circle(5)

print("Rectangle Area:", r.area())  # 15
print("Circle Area:", c.area())