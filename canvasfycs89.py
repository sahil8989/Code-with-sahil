# Importing tkinter module
from tkinter import*

root = Tk()
canvas_width = 500
canvas_height = 500
# Creating Canvas widget
c = Canvas(root, width=500, height=500, bg="blue")
c.pack()
# Creating line in Canvas
y = int(canvas_height/2)
c.create_line(10, y, canvas_width, y, fill="green")
# Creating arc and ovalin canvas
arc = c.create_arc(10, 50, 240, 210, start=90, extent=190, fill="red")
oval = c.create_oval(50, 60, 100, 100)
# Attaching  loop to the program
root.mainloop()
