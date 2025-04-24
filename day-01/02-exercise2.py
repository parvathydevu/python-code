'''Given three points in space A, B and C, determine if the points make a isoceles
   triangle, or right angled triangle or both'''
#solution2
import math

# Coordinates of the points
A = (0, 0, 1)
B = (3, 0, 0)
C = (0, 4, 0)

# Calculate distances between points
d1 = math.sqrt((B[0] - A[0])**2 + (B[1] - A[1])**2 + (B[2] - A[2])**2)
d2 = math.sqrt((C[0] - B[0])**2 + (C[1] - B[1])**2 + (C[2] - B[2])**2)
d3 = math.sqrt((A[0] - C[0])**2 + (A[1] - C[1])**2 + (A[2] - C[2])**2)

# Check if the triangle is isosceles
is_isosceles_triangle = (d1 == d2) or (d2 == d3) or (d1 == d3)

# Check if the triangle is right-angled
sides = sorted([d1, d2, d3])
is_right_angled_triangle = math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2)

# Determine the type of triangle
if is_isosceles_triangle and is_right_angled_triangle:
    print("The points form an isosceles right-angled triangle.")
elif is_isosceles_triangle:
    print("The points form an isosceles triangle.")
elif is_right_angled_triangle:
    print("The points form a right-angled triangle.")
else:
    print("The points do not form an isosceles or right-angled triangle.")