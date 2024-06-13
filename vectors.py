# vectors.py
# A.J. Ristino
# Part of 3D solar system simulator 
# File meant to house the vector class to be used for handling vector calculations in the simulator

import math

class Vector:
    # Three parameters represent value along each axis
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    # Output of this function is to be used to recreate the input object
    # Readable by a Programmer (me) for clarity 
    def __repr__(self):
        return f"Vector({self.x},{self.y},{self.z})"
    
    # returns the actual format for the vectors in line with mathematical representation of vectors
    # this will be used in the simulation:
    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k"
    
    # Below method is for indexing the vector class in order to extract specific values
    def __getitem__ (self, item):
        if item == 0:
            return self.x
        elif item == 1:
            return self.y
        elif item == 2:
            return self.z
        else:
            raise IndexError("Vector class consists of only three components.")
        
    # Next we need to define basic arithmetic functions: addition and subtraction
    def __add__(self, other):
        return Vector(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z,
        )

    def __sub__(self, other):
        return Vector(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z
        )
    
    # For this project I need scalar multiplication in order to do vector calculations
    def __mul__(self, other):
        if isinstance(other, Vector): # Vector dot product
            return (
                self.x * other.x
                + self.y * other.y
                + self.z * other.z
            )
        elif isinstance(other, (int, float)): # Scalar multiplication (multiplying vector by vector)
            return Vector(
                self.x * other,
                self.y * other,
                self.z * other,
            )
        else:
            raise TypeError("operand must be Vector, int, or float")
        
    # can't divide a vector by a vector, but can divide vector by scalar
    def __truediv__(self, other):
        if isinstance(other, (int,float)):
            return Vector(
                self.x / other,
                self.y / other,
                self.z / other,
            )
        else:
            raise TypeError("operand must be int or float")
    
    # Need to add magnitude element to vector object, to do so needed to import math module
    # Square rot of dot product of the vector within itself

    def get_magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
    
    def normalize(self):
        magnitude = self.get_magnitude()
        return Vector(
            self.x / magnitude,
            self.y / magnitude,
            self.z / magnitude,
        )
    
# Tests:
# test = Vector(3,6,9)
# print(test.get_magnitude)
# print(test.normalize())
# print(test.normalize().get_magnitude())


