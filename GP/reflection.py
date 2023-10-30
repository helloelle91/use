import tkinter as tk
import math

coordinates = []
n = int(input("Enter the Number of Vertices: "))
for i in range(n):
    x = int(input(f"Enter the value of x{i+1}: "))
    y = int(input(f"Enter the value of y{i+1}: "))
    coordinates.append((x,y))


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

root = tk.Tk()
root.title("Practice")

canvas = tk.Canvas(root, width = 800, height = 800)
canvas.create_polygon(coordinates, fill="blue", width=1)

reflect(coordinates)

canvas.pack()

root.mainloop()

#Arrow Coordinates [750, 50], [750, 110], [950, 110], [950, 190], [750, 190], [750, 250], [650, 150]
#Value of a 600