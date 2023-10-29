import tkinter

def reflect(coordinates):
    new_coordinates = []
    for x, y in coordinates:
        new_coordinates.append([-x, y])
    return new_coordinates

root = tkinter.Tk()
root.title("Arrow")

coordinates = [[250, 50], [250, 110], [450, 110], [450, 190], [250, 190], [250, 250], [150, 150]]
reflected_coordinates = reflect(coordinates)
print(reflected_coordinates)

canvas = tkinter.Canvas(root, width=800, height=800)
canvas.create_polygon(coordinates, fill="light blue", outline="black", width=4)
canvas.create_polygon(reflected_coordinates, fill="light blue", outline="black", width=4)

canvas.pack()

root.mainloop()
