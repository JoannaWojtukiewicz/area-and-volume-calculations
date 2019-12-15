
import math

class Triangle():
    ''' Class created for calculating surface area of a triangle'''
    
    def __init__(self, a, h):
        self.a = a
        self.h = h

    def __calculate_area(self):
        A = self.a * self.h * 0.5
        return A

    def get_area(self):
        return ('''
                                                             * * * * * * 
                    Surface area of triangle is {:.2f} square units used
                                                             * * * * * * 
        '''.format(self.__calculate_area()))

class Square():
    ''' Class created for calculating surface area of a square'''
    
    def __init__(self, a):
        self.a = a

    def __calculate_area(self):
        A = self.a ** 2
        return A

    def get_area(self):
        return ('''
                                                             * * * * * * 
                     Surface area of square is {:.2f} square units used
                                                             * * * * * *
        '''.format(self.__calculate_area())) 

class Rectangle():
    ''' Class created for calculating surface area of a rectangle'''
    
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __calculate_area(self):
        A = self.a * self.b
        return A

    def get_area(self):
        return ('''
                                                             * * * * * * 
                   Surface area of rectangle is {:.2f} square units used
                                                             * * * * * * 
        '''.format(self.__calculate_area()))

class Cube():
    ''' Class created for calculating surface area and volume of a cube'''
    
    def __init__(self, a):
        self.a = a

    def __calculate_area(self):
        A = 6 * self.a **2
        return A

    def __calculate_volume(self):
        V = self.a ** 3
        return V

    def get_area(self):
        return ('''
                                                             * * * * * * 
                     Surface area of cube is {:.2f} square units used
                                                             * * * * * * 
        '''.format(self.__calculate_area()))

    def get_volume(self):
        return ('''
                                                             * * * * * * 
                     Volume of cube is {:.2f} cubic units used
                                                             * * * * * * 
        '''.format(self.__calculate_volume()))

class RegularPyramid():
    ''' Class created for calculating surface area and volume of a regular pyramid'''
    
    def __init__(self, n, a, h):
        self.n = n
        self.a = a
        self.h = h

    def __calculate_area(self):
        A = 0.25 * self.a * self.n * ( self.a * (1 / math.tan(math.pi / self.n)) + math.sqrt(4 * self.h ** 2 + self.a ** 2 * (1 / math.tan(math.pi / self.n)) ** 2))
        return A

    def __calculate_volume(self):
        V = self.h / 12 * self.n * self.a ** 2 * math.cos(math.pi/self.n)/math.sin(math.pi/self.n)
        return V

    def get_area(self):
        return ('''
                                                             * * * * * * 
                    Surface area of regular pyramid is {:.2f} square units used
                                                             * * * * * * 
        '''.format(self.__calculate_area()))

    def get_volume(self):
        return ('''
                                                             * * * * * * 
                     Volume of regular pyramid is {:.2f} cubic units used
                                                             * * * * * * 
        '''.format(self.__calculate_volume()))
    
class Oval():
    ''' Class created for calculating surface area of a oval'''
    
    def __init__(self, r1, r2):
        self.r1 = r1
        self.r2 = r2

    def __calculate_area(self):
        A = math.pi * self.r1 * self.r2
        return A

    def get_area(self):
        return ('''
                                                             * * * * * * 
                     Surface area of oval is {:.2f} square units used
                                                             * * * * * * 
        '''.format(self.__calculate_area()))




