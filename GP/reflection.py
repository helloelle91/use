import tkinter as tk

coordinates = []
n = int(input("Enter the number of Vertices of the Polygon: "))
for i in range(n):
    x = int(input(f"Enter the x{i} of the point: "))
    y = int(input(f"Enter the y{i} of the point: "))
    coordinates.append((x, y))


def reflect(point,  axis, a):
    if axis == 'x' or axis == 'X':
        return (point[0], -point[1] + 2 * a)
    elif axis == 'y' or axis == 'Y':
        return (-point[0] + 2 * a, point[1])
    else:
        return point
    
axis = input("Enter the axis of reflection (x/y): ")
a = int(input("Enter the value of a: "))

Reflected_coordinates = [reflect(point, axis, a) for point in coordinates]

root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=500)
canvas.create_polygon(coordinates, fill="yellow", outline="black", width=2)
canvas.create_polygon(Reflected_coordinates, fill="red", outline="black", width=2)
canvas.pack()

root.mainloop()

