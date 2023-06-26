"""
Area of a Room.

Write a program that asks the user to enter the width andlength of a room.
Once these values have been read, your program should compute and displaythe area of the room.
The length and the width will be entered as floating-point numbers.
Includeunits in your prompt and output message;
either feet or meters, depending on which unit you aremore comfortable working with.
"""

length = input("Enter lenght in m:")
widths = input("Enter width in m:")
try:
    length = float(length)
    widths = float(widths)
    area = length * widths
except (Exception,):
    print("Non numerical values...")
else:
    print("The area of the room is " + str(area) + "m")
