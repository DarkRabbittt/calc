from tkinter import *
from tkinter import filedialog as fd
from PIL import ImageTk, Image


class InsertImage:
    def __init__(self):
        pass

    def openfn(self):
        filename = fd.askopenfilename(title='open')
        return filename

    def open_img(self):

        path = self.openfn()
        img = Image.open(path)
        width, height = img.size

        ROW_COUNT = 3
        COLUMN_COUNT = 5

        grid_image = Image.new("RGB", (width * COLUMN_COUNT, height * ROW_COUNT), (255, 255, 255))

        for row in range(ROW_COUNT):
            y = row * width

            for column in range(COLUMN_COUNT):
                x = column * height
                grid_image.paste(img, (x, y))

        grid_image.save('~grid_img.png')
        new = "~grid_img.png"
        img = Image.open(new)
        img = img.resize((350, 250), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        return img

    def no_image(self):
        no = ImageTk.PhotoImage(Image.open("./img/no_image.png"))
        return no