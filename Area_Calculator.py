# Welcome Messag eot Area Calc.
print("Welcome to my Area Calculator Program! Simpley name a shape and its size and I will give you the area.")

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

calc()