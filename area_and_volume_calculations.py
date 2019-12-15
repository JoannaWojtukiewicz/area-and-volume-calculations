
# Program for calculating surface areas and volumes of selected figures

from area_and_volume_formulas import Triangle, Square, Rectangle, Cube, RegularPyramid, Oval


def float_type(value):
    ''' Function created to ensure the right type of variable'''
    while type(value) is not float:
        try:
            return float(value)
        except:
            value= input('The value entered must be a number. Try again. ')
        

def main():
    ''' Main function of the logic control program'''  
    choice = None
    print("It's a program for calculating surface areas and volumes of selected figures.")
    while choice != '0':
        print('''

        To choose what you want to calculate select the appropriate number according to the list:

        1 - surface area of triangle
        2 - surface area of  square
        3 - surface area of rectangle
        4 - surface area of cube
        5 - volume of cube
        6 - surface area of regular pyramid
        7 - volume of regular pyramid
        8 - surface area of oval.

        Provide the required data to perform the calculations.

        *** Pay attention! ***
        Enter only numbers in identical units.

        If you want to end the program select 0.  
        ''')

        choice = input('Your choice is: ')

        if choice == '0':
            print('The end')

        elif choice == '1':
            a = float_type(input('Enter the length of the triangle base:  '))
            h = float_type(input('Enter the height of the triangle:  '))
            triangle = Triangle(a, h)
            print(triangle.get_area())      

        elif choice == '2':
            a = float_type(input('Enter the side length of the square: '))
            square = Square(a)
            print(square.get_area())    

        elif choice == '3':
            a = float_type(input('Enter the length of the first side of the rectangle:  '))
            b = float_type(input('Enter the length of the second side of the rectangle:  '))
            rectangle = Rectangle(a, b)
            print(rectangle.get_area())      

        elif choice == '4' or choice == '5':
            a = float_type(input('Enter the side length of the cube: '))
            cube = Cube(a)
            if choice =='4':
                print(cube.get_area())
            else:
                print(cube.get_volume())

        elif choice == '6' or choice == '7':
            n = float_type(input('Enter the number of sides of the base of the regular pyramid: '))
            a = float_type(input('Enter the length of the side of the base of the regular pyramid: '))
            h = float_type(input('Enter the height of the regular pyramid: '))
            regular_pyramid = RegularPyramid(n,a,h)
            if choice == '6':
                print(regular_pyramid.get_area())
            else:
                print(regular_pyramid.get_volume())

        elif choice == '8':
            r1 = float_type(input('Enter the first oval radius: '))
            r2 = float_type(input('Enter the second oval radius: '))
            oval = Oval(r1, r2)
            print(oval.get_area())

        else:
            print('\n \t*** Selected option is not available. Please try again. ***')

        if choice != '0':
            again = None
            while again != 'y':
                again = input('Do you want to continue calculations? Enter y or n ').lower()
                if again == 'n':
                    choice = '0'
                    print('The end')
                    break
               

main()
