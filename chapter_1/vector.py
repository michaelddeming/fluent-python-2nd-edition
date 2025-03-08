
#  import math to use the math.hypot function
import math


# define the Vector class object
class Vector:

    # upon initialization, set x and y to instance variables for self Vector. x and y are 0 be default. 
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    #  repr method should return a string representation of the object at instantiation.
    # !r -> gets the standard representation of the attribute to be displayed
        # Vector(2, 3) vs. Vector('2', '3') (without !r)
    def __repr__(self):
        return f"Vector({self.x!r}, {self.y!r})"
    
    # math.hypot returns the hypotenuse or Euclidean norm (distance between the origin (0,0) and Vector self.)
    def __abs__(self):
        return math.hypot(self.x, self.y)
    
    # return True if the magnitude of the Vector self is greater than 0. Return false if Vector magnitude is 0. 
    def __bool__(self):
        return bool(abs(self))
    
    def __add_(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)