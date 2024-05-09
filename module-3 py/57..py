'''57.Write a Python program to convert degree to radian'''
import math

def degree_to_radian(degree):
    radian = degrees * (math.pi / 180)
    return radian


degrees = 45
radians = degree_to_radian(degrees)
print(f"{degrees} degrees is equal to {radians:.2f} radians.")
