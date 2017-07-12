import math 
#from decimal import Decimal,getcontext
#getcontext().prec = 30
class Vector(object):
    def __init__(self,coordinates):
        try:
            if not coordinates:
                raise ValueError
                #if coordinates is not passed then it will rise Value Error 
            self.coordinates = tuple(coordinates)
            #self.coordinates = tuple([Decimal(x)for x in coordinates])
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
        return 'Vector:{}'.format(self.coordinates)
    def __repr__(self):
        return 'Vector:{}'.format(self.coordinates)
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
            #i=i*Decimal(s)
            i=i*s
            coordinates.append(i)
        return coordinates
    def magnitude(self):
        mag = 0
        for i in self.coordinates:
            i=i*i
            mag =abs(mag+i)
        return math.sqrt(mag)
    
    def magnitude1(self):
        mag = 0
        coordinate_squre=[i*i for i in self.coordinates]
        return math.sqrt(sum(coordinate_squre))
    
#     def normalize(self):
#         try:
#             recip = Decimal(1)/self.magnitude()
#             return Vector(self.scal_mul(recip))
#         except ZeroDivisionError:
#             raise Exception("Can not Normalize Zero Vector")
    def normalize(self):
        try:
            recip = 1/self.magnitude()
            return Vector( self.scal_mul(recip))
        except ZeroDivisionError:
            raise Exception("Can not Normalize Zero Vector")
            
            
            
    def dot_product(self,v):
        mul = self.mul(v)
        return sum(mul)
    
    def dot_product2(self,v):
        self.mul = [x*y for x,y in zip(self.coordinates,v.coordinates)]
        return sum(self.mul)
    
    def angle_rad(self,v):
        norm = self.normalize()
        angle = 1/ math.cos(norm.dot_product2(v))
        return angle

    def angle(self,v,in_degree=False):
        nrm_self = self.normalize()
        nrm_v = v.normalize()
        dot_product_of_norm =round(nrm_self.dot_product2(nrm_v))
        angle_rad = math.acos(dot_product_of_norm)
        if in_degree:
            angle_in_degree = angle_rad * 180./math.pi
            return angle_in_degree
        else:
            return angle_rad
            
    def is_orthogonal(self,v,tolerance=1e-10):
        return self.dot_product2(v)<tolerance
    
    def Parallel(self,v):
        norm1 = self.normalize()
        norm2 = v.normalize()
        ans = norm1.sub(norm2)
        print(ans)
        if ans == 0:
            print ("Parallal")
        else:
            print ("Not Parallal")
            
    def is_zero(self, tolerance=1e-10):
        return self.magnitude() < tolerance
    
    def is_parallel_to(self, v):
        if self.is_zero() or v.is_zero():
            return "True"
        else:
             return "False"
    def par_comp(self,v):
        u1 = self.dot_product( v.normalize())
        return Vector(v.normalize().scal_mul(u1))
    def orth_comp(self,v):
        return self.sub(self.par_comp(v))

    
    def cross(self,v):
        try:
            x1,y1,z1 = self.coordinates
            x2,y2,z2 = v.coordinates
            return Vector([y1*z2- y2*z1,-(x1*z2-x2*z1),x1*y2-x2*y1])
        except ValueError as e :
                error =  str(e)
                if error == "need more than 2 values to unpack" or error == 'not enough values to unpack (expected 3, got 2)':
                    self_pad_with_zero = Vector(self.coordinates+('0',))
                    v_pad_with_zero = Vector(v.coordinates+('0',))
                    return self_pad_with_zero.cross(v_pad_with_zero)
                elif(error =='too many values to unpack'
                     or error == 'need more than 1 value to unpack'
                     or error == "too many values to unpack (expected 3)"):
                    
                    print ( "Cross Product is limited to 3 dimension but given more than 3")
                else:
                    print (error)
                
    def area_parallelogram(self,v):
        u1 = self.cross(v)
        return u1.magnitude()
    
    def area_tringle(self,v):
        u1 = self.cross(v)
        return u1.magnitude()/2
    
v1 = Vector([8.462,7.893,-8.187])
v2 = Vector([6.984,-5.975,4.778])
v1.cross(v2)
v1 = Vector([-8.987,-9.838,5.031])
v2 = Vector([-4.268,-1.861,-8.866])
v1.area_parallelogram(v2)
v1 = Vector([1.5,9.547,3.691])
v2=Vector([-6.007,0.124,5.772])
v1.area_tringle(v2)
   

 # v1=  Vector([3.039,1.879])
# v2=  Vector([0.825,2.036])
# v1. par_comp(v2)
# v1= Vector([-9.88,-3.264,-8.159])
# v2= Vector([-2.155,-9.353,-9.473])
# v1.orth_comp(v2)
# v1= Vector([3.009,-6.172,3.692,-2.51])
# v2= Vector([6.404,-9.144,2.759,8.718])
# v1. par_comp(v2)
#v1.orth_comp(v2)

