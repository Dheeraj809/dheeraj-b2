import math
def segmentarea(r,angle):
    areaofsector = pi * (r * r) * (angle / 360) 
    areaoftriangle = 1 / 2 *(r * r) *math.sin((angle * pi) / 180) 
  
    return areaofsector - areaoftriangle; 
r=int(input("enter the radius"))
angle=int(input("enter the angle"))
print("area of minor segment=",segmentarea(r,angle))
print("area of major segment=",segmentarea(r,(360-angle)))