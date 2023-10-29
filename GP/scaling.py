import tkinter as tk

coordinates = []
for i in range(3):
    x = int(input(f"Enter the x{i} of the point: "))
    y = int(input(f"Enter the y{i} of the point: "))
    coordinates.append((x, y))

Sx = float(input("Enter the scaling factor in the x-direction: "))
Sy = float(input("Enter the scaling factor in the y-direction: "))

root = tk.Tk()
root.title("Practical 2")
canvas = tk.Canvas(root, width=500, height=500)
canvas.create_polygon(coordinates[0][0], coordinates[0][1], coordinates[1][0], coordinates[1][1], coordinates[2][0], coordinates[2][1], fill="blue", width=2)
canvas.create_polygon(coordinates[0][0] * Sx, coordinates[0][1] * Sy, coordinates[1][0] * Sx, coordinates[1][1] * Sy, coordinates[2][0] * Sx, coordinates[2][1] * Sy, fill="green", width=2)
canvas.pack()

root.mainloop()
