import tkinter as tk
import math

coordinates = []
n = int(input("Enter the Number of Vertices: "))
for i in range(n):
    x = int(input(f"Enter the value of x{i+1}: "))
    y = int(input(f"Enter the value of y{i+1}: "))
    coordinates.append((x,y))

def scale(coordinates, n):
    sx = int(input("Enter sx: "))
    sy = int(input("Enter sy: "))
    new_coordinates = []
    for i in range(n):
        new_coordinates.append((coordinates[i][0] * sx, coordinates[i][1] * sy))
    canvas.create_polygon(new_coordinates, fill="green", width=1)

root = tk.Tk()
root.title("Practice")

canvas = tk.Canvas(root, width = 800, height = 800)
canvas.create_polygon(coordinates, fill="blue", width=1)

scale(coordinates, n)

canvas.pack()

root.mainloop()