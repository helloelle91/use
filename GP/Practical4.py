import tkinter as tk
import math

coordinates = []
for i in range(3):
    x = int(input(f"Enter the x{i} of the point: "))
    y = int(input(f"Enter the y{i} of the point: "))
    coordinates.append((x, y))

angle = int(input("Enter the angle of rotation: "))

def rotate(point, angle):
    radians = math.radians(angle)
    x = point[0] * math.cos(radians) - point[1] * math.sin(radians)
    y = point[0] * math.sin(radians) + point[1] * math.cos(radians)
    return (x, y)

rotated_coordinates = [rotate(point, angle) for point in coordinates]

root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=500)
canvas.create_polygon(coordinates, fill="red")
canvas.create_polygon(rotated_coordinates, fill="blue") 
canvas.pack()

root.mainloop()