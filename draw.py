import numpy as np
from tkinter import *             # GUI used for displaying drawings
from PIL import Image, ImageDraw  # depends on Pillow, used for drawing images

from sklearn.preprocessing import normalize
from scipy.ndimage.interpolation import shift
from scipy.ndimage.measurements import center_of_mass
from scipy.misc import imresize, imshow, imsave

# convert to numpy matrix (load image)
# sklearn model.predict

click_held = False
click_coord = None
d_size = 256  # draw image size, 256x256 canvas
f_size = 8    # final image size, want 8x8

root = Tk()
im = Image.new('L', (d_size, d_size), 255)
d = ImageDraw.Draw(im)

def main():
    drawing_area = Canvas(root, background='#FFF', width=d_size, height=d_size)
    drawing_area.pack()
    drawing_area.bind("<Motion>", motion)
    drawing_area.bind("<ButtonPress-1>", click_press)
    drawing_area.bind("<ButtonRelease-1>", click_release)
    drawing_area.bind("<Return>", done)
    drawing_area.focus_set()
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
            event.widget.create_line(*click_coord, event.x, event.y, width=4,
                                     smooth=True)
            d.line([click_coord, (event.x, event.y)], width=4, fill='#000')
        click_coord = event.x, event.y

def done(event):
    root.quit()
    imsave('img.png', post_process(im))

def post_process(img):
    im_arr = 1 - (np.array(img)/255)  # invert and normalize image
    im_arr = bbox(im_arr)

    im_arr = imresize(im_arr, size=f_size/max(*im_arr.shape), interp='bicubic')
    im_arr = normalize(im_arr)  # bicubic messes with our normalized values
    im_arr = np.pad(im_arr, ((0,0), np.subtract((f_size, f_size), im_arr.shape)), mode='constant')

    diff = np.subtract((f_size/2, f_size/2), center_of_mass(im_arr))
    im_arr = shift(im_arr, diff, order=0)  # center our digit in an 8x8 image
    return 1 - im_arr

def bbox(img):
    """find bounding box for an array, stripping surrounding zero elements"""
    rows = np.any(img, axis=1)
    cols = np.any(img, axis=0)
    rmin, rmax = np.where(rows)[0][[0, -1]]
    cmin, cmax = np.where(cols)[0][[0, -1]]
    return img[rmin:rmax, cmin:cmax]

if __name__ == "__main__":
    main()
