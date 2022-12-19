import os
from tkinter import *
from PIL import ImageTk, Image
from wallpaper_window import WallpaperWindow
from laminate_window import LaminateWindow
from tile_window import TileWindow


class Window:
    def __init__(self, title="Калькулятор ремонта", resizable=(False, False)):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry("600x600+460+200")
        self.root.resizable(resizable[0], resizable[1])
        self.logo = ImageTk.PhotoImage(Image.open("./img/back.png"))
        self.back = Label(self.root, image=self.logo)
        self.back.place(x=420, y=150, anchor="c")

    def run(self):
        self.root.mainloop()

    def create_wchild(self, title="Расчет количества обоев", resizable=(False, False)):
        WallpaperWindow(self.root, title, resizable)

    def create_lchild(self, title="Расчет количества ламината", resizable=(False, False)):
        LaminateWindow(self.root, title, resizable)

    def create_tchild(self, title="Расчет количества плитки", resizable=(False, False)):
        TileWindow(self.root, title, resizable)


if __name__ == "__main__":
    window = Window()
    ButtonWP = Button(text="Рассчитать количество обоев", font=('Times', 16), command=window.create_wchild, width=30, height=3,
                      bg="#FF1493", fg="#FFFFFF", activebackground="#DC143C", activeforeground="#FFFFFF")
    ButtonWP.place(x=300, y=100, anchor="c")
    ButtonLM = Button(text="Рассчитать количество ламината", font=('Times', 16), command=window.create_lchild, width=30, height=3,
                      bg="#FF1493", fg="#FFFFFF", activebackground="#DC143C", activeforeground="#FFFFFF")
    ButtonLM.place(x=300, y=200, anchor="c")
    ButtonTL = Button(text="Рассчитать количество плитки", font=('Times', 16), command=window.create_tchild, width=30, height=3,
                      bg="#FF1493", fg="#FFFFFF", activebackground="#DC143C", activeforeground="#FFFFFF")
    ButtonTL.place(x=300, y=300, anchor="c")
    window.run()
    os.remove("grid_img.png")