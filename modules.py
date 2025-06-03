import random
import string
import math
from datetime import datetime

# Generate password
# Generate password
def generate_password(num):
    if num <= 8:
        print("Password must be longer than 8 characters!")
        return  # To exit the function if the length is invalid
    else:
        # string.ascii_letters > predefined string that contains all the lowercase and uppercase ASCII letters, from 'a' to 'z' and 'A' to 'Z'.
        # string.digits > predefined string that contains all digits from '0' to '9'
        letters_and_digits = string.ascii_letters + string.digits  # Letters (upper & lower) + digits

        # Create the password by randomly picking characters
        password = ""  # starts empty
        for i in range(num):  # loop to add random characters to password
            password += random.choice(letters_and_digits) 
            # random.choice() is a function from Python's random module that picks a random element from the provided sequence 
        return password

print(generate_password(8))  
print(generate_password(20))  



#Calculate the difference in days between the two dates and return the result.
def date_diff(dateT1, dateT2):
#Take two strings in the format “YYYY-MM-DD” as input.
#Use the datetime module to convert these strings into datetime objects.  
# I googled this and found strptime, will convert the string into objects 
# This method sbescially converts "2023-01-01" to datetime(2023, 1, 1, 0, 0) > which we can use to do math .... somehow
    date1 = datetime.strptime(dateT1, '%Y-%m-%d')  
    date2 = datetime.strptime(dateT2, '%Y-%m-%d')

 
    print(date1) # converts "2025-04-14" to datetime(2025, 4, 14)
    print(date2) # converts "2025-07-21"" to datetime(2025, 7, 21) 
    # Then it does the date math > calculate the difference in days
    diff_time = date2 - date1
    return diff_time 

print(date_diff("2025-04-14", "2025-07-21"))




#Calculate area
def calculate_circle_area(radius):
    #Take a number as input. This number will be the radius of a circle.
    # Utilize the pi constant from the math module to help calculate the area of the circle.
    # Return the area of the circle > Area = PI * r^2
    
    area = math.pi * (radius ** 2)
    return area
print(calculate_circle_area (4))

