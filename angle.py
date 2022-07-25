import math

def angle(x1,y1,x2,y2,x3,y3):
    # (x1,y1) - one end
    # (x2,y2) - pivot
    # (x3,y3) - other end 
    num = (x1-x2)*(x3-x2)+(y1-y2)*(y3-y2)
    deno = math.sqrt(((x1-x2)**2 + (y1-y2)**2)*((x3-x2)**2 + (y3-y2)**2))
    angle_rad = math.acos(num/deno)
    angle_deg = angle_rad*180/math.pi
    print("angle (rad) = " + str(angle_rad))
    print("angle (deg) = " + str(angle_deg))
