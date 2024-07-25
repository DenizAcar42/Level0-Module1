# Write a Python program that asks the user for the radius of a circle.

# Next, ask the user if they would like to calculate the area or circumference of a circle.
# If they choose area, display the area of the circle using the radius.
# Otherwise, display the circumference of the circle using the radius.

#Area = πr^2
#Circumference = 2πr
# Write a Python program that asks the user for the radius of a circle.
import math
from tkinter import simpledialog, messagebox

radius = simpledialog.askinteger(title="circle calc", prompt="What is the radius of your circle?")
# Next, ask the user if they would like to calculate the area or circumference of a circle.
name = simpledialog.askstring(title="circle calc", prompt="Would you like to calculate the area of the circumference of your circle?")

# If they choose area, display the area of the circle using the radius.
if name == "area":
    area = math.pi*radius*radius
elif name == "circumference":
    circ = math.pi*radius*2
# Otherwise, display the circumference of the circle using the radius.
else:
    messagebox.showinfo("Please correctly spell either, -area- or -circumference-")
#Area = πr^2
#Circumference = 2πr