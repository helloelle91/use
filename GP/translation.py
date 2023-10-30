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

root = tk.Tk()
root.title("Practice")

canvas = tk.Canvas(root, width = 800, height = 800)
canvas.create_polygon(coordinates, fill="blue", width=1)

translate(coordinates, n)

canvas.pack()

root.mainloop()