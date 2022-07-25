import math
from re import L
from telnetlib import X3PAD

def angle_rad(x1,y1,x2,y2,x3,y3):
    # (x1,y1) - one end
    # (x2,y2) - pivot
    # (x3,y3) - other end 
    num = (x1-x2)*(x3-x2)+(y1-y2)*(y3-y2)
    deno = math.sqrt(((x1-x2)**2 + (y1-y2)**2)*((x3-x2)**2 + (y3-y2)**2))
    angle_rad = math.acos(num/deno)
    return angle_rad

def angle_deg(angle_rad):
    angle_deg = angle_rad*180/math.pi
    return angle_deg
