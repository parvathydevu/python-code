'''Given three points in space A, B and C, determine if the points make a isoceles
   triangle, or right angled triangle or both'''
#Solution2
import math

#Get user input for the coordinates of the points
x1, y1, z1 = map(float, input("Enter coordinates of point A (x y z): ").split())
x2, y2, z2 = map(float, input("Enter coordinates of point B (x y z): ").split())
x3, y3, z3 = map(float, input("Enter coordinates of point C (x y z): ").split())

# Coordinates of the points
A = (x1, y1, z1)
B = (x2, y2, z2)
C = (x3, y3, z3)

# Calculate distances between points
d1 = math.sqrt((B[0] - A[0])**2 + (B[1] - A[1])**2 + (B[2] - A[2])**2)
d2 = math.sqrt((C[0] - B[0])**2 + (C[1] - B[1])**2 + (C[2] - B[2])**2)
d3 = math.sqrt((A[0] - C[0])**2 + (A[1] - C[1])**2 + (A[2] - C[2])**2)

# Check if the triangle is isosceles
is_isosceles_triangle = (d1 == d2) or (d2 == d3) or (d1 == d3)

# Check if the triangle is right-angled
# Identify the longest side- longest side is hypotenuse
if d1 > d2 and d1 > d3:
    hypotenuse = d1
    side1 = d2
    side2 = d3
elif d2 > d1 and d2 > d3:
    hypotenuse = d2
    side1 = d1
    side2 = d3
else:
    hypotenuse = d3
    side1 = d1
    side2 = d2

is_right_angled_triangle= hypotenuse**2, side1**2 + side2**2 #hyp2=sum of sq of smallest sides

# Determine the type of triangle
if is_isosceles_triangle and is_right_angled_triangle:
    print("The points forms both isosceles and right-angled triangle.")
elif is_isosceles_triangle:
    print("The points form an isosceles triangle.")
elif is_right_angled_triangle:
    print("The points form a right-angled triangle.")
else:
    print("The points do not form an isosceles or right-angled triangle.")