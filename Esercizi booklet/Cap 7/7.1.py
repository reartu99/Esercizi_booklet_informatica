"""
Write a Python program to calculate the arc length of an angle by assigning values to the radius
and angle data Attributes of the class ArcLength
"""

import numpy as np


class ArcLength:
    def __init__(self, rad, ang):
        self.rad = rad
        self.ang = ang

    def value_arc_len(self):
        return 2*np.pi*self.rad*self.ang/360


A = ArcLength(1, 1)
print(A.value_arc_len())
