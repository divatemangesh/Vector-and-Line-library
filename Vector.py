import math 
class Vector(object):
    def __init__(self,coordinates):
        try:
            if not coordinates:
                raise ValueError
                #if coordinates is not passed then it will rise Value Error 
            self.coordinates = list(coordinates)
            #Outside Class :-Vector.coordinates will give print vectors in tuple form
            #Inside Class :- self.coordinates will print vectors in tuple form
            self.dimension = len(coordinates)
            #Outside Class :-Vector.dimension will print vectors dimension/size
            #Inside Class :- self.dimension will print vectors dimension/size
        except ValueError:
            raise ValueError('The coordinates must be non empty')
        except TypeError:
            raise TypeError('The coordinates must be itterable')
    def __str__(self):
        return 'Vector:{}'.format(self,coordinates)
    def __eq__(self,v):
        return self.coordinates == v.coordinates
    def add (self,v):
        coordinates=[]
        for i in range(0,self.dimension):
            i=self.coordinates[i]+v.coordinates[i]
            coordinates.append(i)
        return coordinates
            
    def sub (self,v):
        coordinates=[]
        for i in range(0,self.dimension):
            i=self.coordinates[i]-v.coordinates[i]
            coordinates.append(i)
        return coordinates
    
    def scal_mul(self,s):
        coordinates=[]
        for i in self.coordinates:
            i=i*s
            coordinates.append(i)
        return coordinates
    def magnitude(self):
        mag = 0
        for i in self.coordinates:
            i=i*i
            mag =mag+i
        return math.sqrt(mag)
    
    def magnitude1(self):
        mag = 0
        coordinate_squre=[i*i for i in self.coordinates]
        return math.sqrt(sum(coordinate_squre))
    
    def normalize(self):
        try:
            recip = 1/self.magnitude()
            return Vector([self.scal_mul(recip)])
        except ZeroDivisionError:
            raise Exception("Can not Normalize Zero Vector")
    
