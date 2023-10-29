import tkinter as tk
import math

def shear(point,theta):
    radians = math.radians(theta)
    x = point[0] + point[1] * math.tan(radians)
    y = point[1]
    return (x, y)



coordinates = []
for i in range(4):
    x = int(input(f"Enter the x{i+1} coordinate of the rectangle: "))
    y = int(input(f"Enter the y{i+1} coordinate of the rectangle: "))
    coordinates.append((x, y))
theta = int(input("Enter the angle of rotation: "))



root = tk.Tk()
root.title("Rectangle Shear")

canvas = tk.Canvas(root, width=800, height=500)
canvas.create_polygon(coordinates[0], coordinates[1], coordinates[2], coordinates[3],fill="", outline="red")
canvas.create_polygon(shear(coordinates[0],theta), coordinates[1], coordinates[2], shear(coordinates[3],theta), 
                      fill="", outline="blue")

canvas.pack()

root.mainloop()