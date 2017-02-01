import math

class Point:
    'Represents a point in two-dimensional coordinates'
    
    def __init__(self,  x=0,  y=0):
        "Initialize the position of a new point. The x and y coordinates can be specified. If they are not, the points defaults to the origin."
        self.move(x, y)
        
    def reset(self):
        self.x = 0
        self.y = 0
        
    def move(self,  x,  y):
        self.x = x
        self.y = y
        
    def calculate_distance(self,  other_point):
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y) ** 2)
