import math

#    Validates if the input 'age' is a positive integer AND if its an int type or something else. 
def validate_age(age):
    if int(age) <= 0:
        raise ValueError("Age must be a positive integer.")
    return age

print(validate_age(2.5))

#Calculate the area of a rectangle.
def calculate_rectangle_area(length, width):
    
    #Calculate the area of a rectangle.
    #length: The length of the rectangle.
    #width: The width of the rectangle.
    #It will returns the area of the rectangle.
   
    return length * width

print(calculate_rectangle_area(4,2))

#Calculate the area of a circle.

def calculate_circle_area(radius):
    #radius: The radius of the circle.
    
    # Use the import math for the pi value
    return math.pi * radius ** 2
print(calculate_circle_area(3))


#Determine the area of the given shape (rectangle or circle) based on the provided dimensions

def get_area(shape, *args):
    # takes the shape as string, and I was thinking about if someone wrote in caps, so I used .lower()
    # *args > since rectangle needs 2, and circle 1, we are using args because it will allow either one or two to numbers to be added 
    if shape.lower() == "rectangle":
        if len(args) != 2: 
            #checks if the args actually has two numbers and not less more or less. 
            raise ValueError("Rectangle needs two arguments > length and width. Can't work on just one sorry.") 
            #using what we learned from the first assignment. 
            
        # we are assigning length and width the values from args
        length = args[0] #assign the first number in the list to length
        width = args[1] #assign the second number to width
    
        return calculate_rectangle_area(length, width)
    
    elif shape.lower() == "circle":
        if len(args) != 1:
            #checks if the args has atleast one, and can't exceed cause its a circle.
            raise ValueError("Circle requires one arg: radius.")
        radius = args[0] 
           # assign the first number in args to radius 
        return calculate_circle_area(radius)
    
    else:
        raise ValueError("Unsupported shape. Please use 'rectangle' or 'circle'.")
    
print(get_area('CIRCLE', 7))
print(get_area('rectangle', 3, 4))