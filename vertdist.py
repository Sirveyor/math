import numpy as np
from dms_to_dd import dms_to_dd



"""script to compute the vertical distance of a foresight 
"""


# get the users input


user_input = input("Enter Zenith Angle, Slope Distance, Point Elevation, Instrument Height, Rod Height: ")


print("You entered {}", format(user_input))
value = user_input.split(',')
angle = value[0]
dist = value[1]
p1z = float(value[2])
ih = float(value[3])
rh = float(value[4])


vd = np.cos(dms_to_dd(angle) * np.pi / 180) * float(dist)
p2z = p1z + ih + vd - rh
print(p2z)


