# Import math module for pi
import math

# Welcome Messag eot Area Calc.
print("Welcome to my Area Calculator Program! Simpley name a shape and its size and I will give you the area.")
print("ENter the folowing shpaes: square, rectangle, triangle, circle, parallelogram, trapezoid")

# Function to create area Calculator
## First create input statement requeting input for the shape they want to get the area for
def calc():
    shape_request = (input("Please input a shape you would like to get the area for: "))
    ### Keep input in lower case
    shape_request = shape_request.lower()

    ## If the shape they input is *input shape* show their input and request info on length and width
    if shape_request == "square":
        print("You input square!")
        square_length = int(input("What is the length? "))
        square_width = int(input("What is the width? "))
        total_area = int(square_length * square_width)
        print("The area is: " + format(total_area))
    # ELif statements for other shapes
    elif shape_request == "rectangle":
        print("You input rectangle!")
        rec_length = int(input("What is the length? "))
        rec_width = int(input("What is the width? "))
        total_area = int(rec_length * rec_width)
        print("The area is: " + format(total_area))
    elif shape_request == "parallelogram":
        pel_length = int(input("What is the length? "))
        pel_width = int(input("What is the width? "))
        total_area = int(pel_length * pel_width)
        print("The area is: " + format(total_area))
    elif shape_request == "trapezoid":
        trap_base_1 = int(input("What is base 1? "))
        trap_base_2 = int(input("What is base 2? "))
        trap_height = int(input("What is the height? "))
        total_area = float(0.5 * (trap_base_1 + trap_base_2) * trap_height)
        print("The area is: " + format(total_area))
    elif shape_request == "triangle":
        tri_base = int(input("What is the base? "))
        tri_height = int(input("What is the height? "))
        total_area = float(0.5 * tri_base * tri_height)
        print("The area is: " + format(total_area))
    elif shape_request == "circle":
        radius = int(input("What is the radius? "))
        # Using pi from math module
        total_area = float(math.pi * radius ** 2)
        print("The area is: " + format(total_area))

    else:
        print("Sorry thats not a shape!")

calc()