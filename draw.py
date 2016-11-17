from tkinter import *
from pillow import ImageDraw

# convert to numpy matrix (load image)
# sklearn model.predict

click_held = False
click_coord = None

def main():
    root = Tk()
    drawing_area = Canvas(root, background='white', width=256, height=256)
    drawing_area.pack()
    drawing_area.bind("<Motion>", motion)
    drawing_area.bind("<ButtonPress-1>", click_press)
    drawing_area.bind("<ButtonRelease-1>", click_release)
    root.mainloop()

def click_press(event):
    global click_held
    click_held = True

def click_release(event):
    global click_held, click_coord
    click_held = False
    click_coord = None

def motion(event):
    if click_held:
        global click_coord
        if click_coord:
            event.widget.create_line(*click_coord, event.x, event.y, width=3,
                                     smooth=True)
        click_coord = event.x, event.y

if __name__ == "__main__":
    main()
