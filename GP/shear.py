import tkinter as tk
import math

coordinates = []
n = int(input("Enter the Number of Vertices: "))
for i in range(n):
    x = int(input(f"Enter the value of x{i+1}: "))
    y = int(input(f"Enter the value of y{i+1}: "))
    coordinates.append((x,y))

def shear(coordinates, n):
    theta = int(input("Enter the Angle of Shearing: "))
    radians = math.radians(theta)
    new_coordinates = []
    for i in range(n):
        new_coordinates.append((coordinates[i][0] + coordinates[i][1]* math.tan(radians), coordinates[i][1]))
    canvas.create_polygon(new_coordinates, fill="yellow", width=1)

root = tk.Tk()
root.title("Practice")

canvas = tk.Canvas(root, width = 800, height = 800)
canvas.create_polygon(coordinates, fill="blue", width=1)

shear(coordinates, n)

canvas.pack()

root.mainloop()