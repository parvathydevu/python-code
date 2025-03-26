'''Write a program to calculate the height of a building given the 
   distance of the measuring instrument from the building and angle formed 
   at the observer when the highest point is seen'''
#Solution1
#Input
import math
feet = float(input("Enter the feet from the building (feet): "))
angle = float(input("Enter the angle of elevation (in degrees): "))

#process
angle_rad=math.radians(angle)  #rad= angle*pi/180
d=feet*0.3048 #in meters

#output)
height=d*math.tan(angle_rad)
print("The height of the building is:", height,"meters")