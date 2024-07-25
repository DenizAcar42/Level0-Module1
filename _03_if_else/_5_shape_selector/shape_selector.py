import turtle
from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Make a new turtle
    deniz = turtle.Turtle()
    # Ask the user what shape they want to draw and store it in a variable
    shape = simpledialog.askstring(title="awr", prompt="What shape would u like to deaw triangle square or circle")
    # Draw the shape requested by the user using if-elif-else statements
    if shape == "triangle":
        deniz.penup()
        deniz.goto(0, 0)
        deniz.pendown()
        deniz.right(60)
        deniz.forward(100)
        deniz.right(60)
        deniz.forward(100)
        deniz.right(60)
        deniz.forward(100)
    elif shape == "square":
        deniz.penup()
        deniz.goto(0, 0)
        deniz.pendown()
        deniz.forward(100)
        deniz.right(90)
        deniz.forward(100)
        deniz.right(90)
        deniz.forward(100)
        deniz.right(90)
        deniz.forward(100)
    else:
        deniz.penup()
        deniz.goto(0, 0)
        deniz.pendown()
        deniz.circle(100)
    # Call the turtle .done() method
