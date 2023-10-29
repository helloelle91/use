import tkinter as tk

coordinates = []
for i in range(2):
    x = int(input(f"Enter the x{i} of the point: "))
    y = int(input(f"Enter the y{i} of the point: "))
    coordinates.append((x, y))

tx = int(input("Enter the translation factor in the x-direction: "))
ty = int(input("Enter the translation factor in the y-direction: "))

root = tk.Tk()
root.title("Practical 1")

canvas = tk.Canvas(root, width=500, height=500)
canvas.create_rectangle(coordinates[0][0], coordinates[0][1], coordinates[1][0], coordinates[1][1], fill="blue", width=2)
canvas.create_rectangle(coordinates[0][0] + tx, coordinates[0][1] + ty, coordinates[1][0] + tx, coordinates[1][1] + ty, fill="green", width=2)

canvas.pack()

root.mainloop()