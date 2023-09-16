import numpy as np
from dms_to_dd import dms_to_dd



"""script to compute the vertical distance of a foresight 
"""

#user_input_za = ()
#user_input_sd = ()




user_input = input("Enter Zenith Angle, Slope Distance: ")
print("You entered {}", format(user_input))
angle = user_input.split(',')[0]
dist = user_input.split(',')[1]

vd = np.cos(dms_to_dd(angle) * np.pi / 180) * float(dist)

print(vd)


