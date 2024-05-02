## import modules
import math

x1 = int(input('Enter the value of x1:\t'))  # the int to typecast string input to integer
x2 = int(input('Enter the value of x2:\t'))
y1 = float(input('Enter the value of y1:\t'))  # float() to typecast string input to float 
y2 = float(input('Enter the value of y2:\t'))

#expressions
simple_expression = (x1 - x2) ** 2 + (y1 - y2) ** 2
d = math.sqrt(simple_expression)

print(f"The distance between the points is: {d}")