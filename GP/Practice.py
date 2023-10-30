import tkinter as tk
import math

coordinates = []
n = int(input("Enter the Number of Vertices: "))
for i in range(n):
    x = int(input(f"Enter the value of x{i+1}: "))
    y = int(input(f"Enter the value of y{i+1}: "))
    coordinates.append((x,y))


def translate(coordinates, n):
    tx = int(input("Enter tx: "))
    ty = int(input("Enter ty: "))
    new_coordinates = []
    for i in range(n):
        new_coordinates.append((coordinates[i][0] + tx, coordinates[i][1] + ty))
    canvas.create_polygon(new_coordinates, fill="red", width=1)

def scale(coordinates, n):
    sx = int(input("Enter sx: "))
    sy = int(input("Enter sy: "))
    new_coordinates = []
    for i in range(n):
        new_coordinates.append((coordinates[i][0] * sx, coordinates[i][1] * sy))
    canvas.create_polygon(new_coordinates, fill="green", width=1)

def reflect(coordinates):
    axis = input("Enter the Axis to relfect on:(X/Y) ").lower()
    a = int(input("Enter the Value of a: "))
    new_coordinates = []
    if axis == 'x':
        for i in range(n):
            new_coordinates.append((coordinates[i][0], -coordinates[i][1] + 2*a))
        canvas.create_polygon(new_coordinates, fill="yellow", width=1)
    else:
        for i in range(n):
            new_coordinates.append((-coordinates[i][0] + 2*a, coordinates[i][1]))
        canvas.create_polygon(new_coordinates, fill="yellow", width=1)

def shear(coordinates, n):
    theta = int(input("Enter the Angle of Shearing: "))
    radians = math.radians(theta)
    new_coordinates = []
    for i in range(n):
        new_coordinates.append((coordinates[i][0] + coordinates[i][1]* math.tan(radians), coordinates[i][1]))
    canvas.create_polygon(new_coordinates, fill="yellow", width=1)

def rotate(coordinates, n):
    theta = int(input("Enter the Angle of Rotation: "))
    radians = math.radians(theta)
    new_coordinates = []
    for i in range(n):
        new_coordinates.append((coordinates[i][0]* math.cos(radians) - coordinates[i][1]* math.sin(radians),
                                coordinates[i][0]* math.sin(radians) + coordinates[i][1]* math.cos(radians)))
    canvas.create_polygon(new_coordinates, fill="grey", width=1)

root = tk.Tk()
root.title("Practice")

canvas = tk.Canvas(root, width = 800, height = 800)
canvas.create_polygon(coordinates, fill="blue", width=1)

# translate(coordinates, n)
# scale(coordinates, n)
# reflect(coordinates)
# shear(coordinates, n)
# rotate(coordinates, n)

canvas.pack()

root.mainloop()