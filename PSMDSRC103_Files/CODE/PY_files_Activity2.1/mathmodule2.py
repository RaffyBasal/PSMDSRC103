import math

def angle_demo():
    angle = math.sin(math.pi/2)
    # the default inpit is in radius
    #t angle sin(90)=1 om degree == sin(pi/2)=1 in radians
    print(angle)
    # to make it convenient, convert it to radians
    angle = math.sin(math.radians(90))
    print(angle)
    #thi is also similar for cosine and other trigometric and hyperbolic function

angle_demo()