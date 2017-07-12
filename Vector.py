    import math 
    class Vector(object):
        def __init__(self,coordinates):
            try:
                if not coordinates:
                    raise ValueError
                    #if coordinates is not passed then it will rise Value Error 
                self.coordinates = tuple(coordinates)
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

        def mul(self,v):
            coordinates=[]
            for i in range(0,self.dimension):
                i=self.coordinates[i]*v.coordinates[i]
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
                return Vector(self.scal_mul(recip))
            except ZeroDivisionError:
                raise Exception("Can not Normalize Zero Vector")

        def dot_product(self,v):
            mul = self.mul(v)
            return sum(mul)

        def dot_product2(self,v):
            self.mul = [x*y for x,y in zip(self.coordinates,v.coordinates)]
            return sum(self.mul)
        #-----------------angle functionn is giving wrong answer-------------
        def angle_rad(self,v):
            norm = self.normalize()
            angle = 1/ math.cos(norm.dot_product2(v))
            return angle

        def angle(self,v,in_degree=False):
            nrm_self = self.normalize()
            nrm_v = v.normalize()
            angle_rad = math.acos(nrm_self.dot_product2(nrm_v))
            if in_degree:
                angle_in_degree = angle_rad * 180./math.pi
                return angle_in_degree
            else:
                return angle_rad


    v1 = Vector([7.887,4.138])
    v2 = Vector([-8.802,6.776])
    print(v1.angle(v2))        
    v3 = Vector([-7.579,-7.88])
    v4 = Vector([22.737,23.64])
    v3.angle(v4)
    
