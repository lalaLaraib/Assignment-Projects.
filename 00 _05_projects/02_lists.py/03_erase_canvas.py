"""
This program creates a canvas with a blue grid and an eraser tool. 
The eraser moves with the mouse and changes grid cells to white upon contact.
"""

import tkinter as tk

# canvas size
CANVAS_WIDTH = 500
CANVAS_HEIGHT = 500
CELL_SIZE = 50  

# Function to create blue grid cells
def create_grid():
    for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
        for col in range(0, CANVAS_WIDTH, CELL_SIZE):
            rect = canvas.create_rectangle(col, row, col + CELL_SIZE, row + CELL_SIZE, fill="blue", outline="white")
            grid_cells.append(rect) 

# Function to move eraser and erase cells
def move_eraser(event):
    # Set eraser position based on mouse movement
    canvas.coords(eraser, event.x - ERASER_SIZE // 2, event.y - ERASER_SIZE // 2,
                  event.x + ERASER_SIZE // 2, event.y + ERASER_SIZE // 2)
    
    # check which rectangles are being erased
    for rect in grid_cells:
        x1, y1, x2, y2 = canvas.coords(rect)
        ex1, ey1, ex2, ey2 = canvas.coords(eraser)
        
        # If eraser overlaps with the rectangle, make it white
        if not (x2 < ex1 or x1 > ex2 or y2 < ey1 or y1 > ey2):  
            canvas.itemconfig(rect, fill="white")

# Main window setup
root = tk.Tk()
root.title("Eraser on Canvas")

# create a canvas
canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
canvas.pack()

# storing cell ids
grid_cells = []
create_grid()

# create an eraser 
ERASER_SIZE = 50
eraser = canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE, fill="gray", outline="black")

canvas.bind("<B1-Motion>", move_eraser)

root.mainloop()