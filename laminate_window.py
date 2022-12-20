import os
from tkinter import *
from tkinter import Entry
import math
from PIL import ImageTk, Image
from tkinter import messagebox
from imgg import InsertImage


class LaminateWindow:
    def __init__(self, parent, title="Окно", resizable=(False, False)):
        self.root = Toplevel(parent)
        self.root.title(title)
        self.root.geometry("800x650+350+150")
        self.root.resizable(resizable[0], resizable[1])
        self.root["background"] = "white"
        self.root.lift()
        self.logo = ImageTk.PhotoImage(Image.open("./img/back.png"))
        self.back = Label(self.root, image=self.logo)
        self.back.place(x=420, y=150, anchor="c")
        self.draw_widgets()
        self.grab_focus()

    def grab_focus(self):
        self.root.grab_set()
        self.root.focus_set()
        self.root.wait_window()

    def price_callback(self):
        str_price = DoubleVar()
        Label(self.root, text="Введите стоимость", width="15", bg="#DC143C", fg="#FFFFFF", font=("Times", 12)).place(x=285, y=210, anchor="c")
        self.price = Entry(self.root, textvariable=str_price)
        self.price.place(x=285, y=240, anchor="c")

    def image(self):
        try:
            self.pic.destroy()
            self.pic_label.destroy()
            insert = InsertImage()
            self.no_img = insert.no_image()
            self.no_image = Label(self.root, image=self.no_img)
            self.no_image.place(x=415, y=14)
            os.remove("~grid_img.png")
        except AttributeError:
            messagebox.showinfo('Внимание!', 'Вы не выбрали изображение')

    def img_label(self):
        try:
            insert = InsertImage()
            self.copy_img = insert.open_img()
            self.pic = Label(self.root, image=self.copy_img)
            self.pic.place(x=415, y=170, anchor="w")
            self.pic_label = Label(self.root, text="Ваш ламинат будет выглядеть так:", width="25", bg="#DC143C", fg="#FFFFFF", font=("Times", 12))
            self.pic_label.place(x=415, y=14)
            self.no_image.destroy()
        except AttributeError:
            messagebox.showinfo('Внимание!', 'Вы не выбрали изображение')

    def draw_widgets(self):
        str_length = DoubleVar()
        str_width = DoubleVar()
        str_l_board = DoubleVar()
        str_w_board = DoubleVar()
        str_board = IntVar()

        self.entry_length = Entry(self.root, textvariable=str_length)
        self.entry_width = Entry(self.root, textvariable=str_width)
        self.entry_str_l_board = Entry(self.root, textvariable=str_l_board)
        self.entry_str_w_board = Entry(self.root, textvariable=str_w_board)
        self.entry_str_board = Entry(self.root, textvariable=str_board)

        self.entry_width.place(x=80, y=50, anchor="c")
        self.entry_length.place(x=80, y=100, anchor="c")
        self.entry_str_l_board.place(x=80, y=150, anchor="c")
        self.entry_str_w_board.place(x=80, y=200, anchor="c")
        self.entry_str_board.place(x=80, y=270, anchor="c")

        insert = InsertImage()
        self.no_img = insert.no_image()
        self.no_image = Label(self.root, image=self.no_img)
        self.no_image.place(x=415, y=14)

        Label(self.root, text="Длина комнаты, м", width="15", bg="#DC143C", fg="#FFFFFF", font=("Times", 12)).place(x=80, y=25, anchor="c")
        Label(self.root, text="Ширина комнаты, м", width="15", bg="#DC143C", fg="#FFFFFF", font=("Times", 12)).place(x=80, y=75, anchor="c")
        Label(self.root, text="Ширина доски, мм", width="15", bg="#DC143C", fg="#FFFFFF", font=("Times", 12)).place(x=80, y=125, anchor="c")
        Label(self.root, text="Длина доски, мм", width="15", bg="#DC143C", fg="#FFFFFF", font=("Times", 12)).place(x=80, y=175, anchor="c")
        Label(self.root, text="Количество досок \n в одной пачке", width="15", bg="#DC143C", fg="#FFFFFF", font=("Times", 12)).place(x=80, y=235, anchor="c")

        Label(self.root, text="Вариант укладки", width="15", bg="#DC143C", fg="#FFFFFF", font=("Times", 12)).place(x=285, y=25, anchor="c")

        Button(self.root, text="Выбрать файл", command=self.img_label, width="20", bg="#DC143C", fg="#FFFFFF",
               activebackground="#FF1493", activeforeground="#FFFFFF", font=("Times", 12)).place(x=285, y=323, anchor="c")
        Button(self.root, text="Удалить изображение", command=self.image, width="20", bg="#DC143C", fg="#FFFFFF",
               activebackground="#FF1493", activeforeground="#FFFFFF", font=("Times", 12)).place(x=285, y=358, anchor="c")
        Button(self.root, text="Рассчитать", command=self.button_action, bg="#DC143C", fg="#FFFFFF",
               activebackground="#FF1493", activeforeground="#FFFFFF", font=("Times", 12)).place(x=250, y=460)
        Button(self.root, text="Вернуться назад", command=self.root.destroy, bg="#DC143C", fg="#FFFFFF", 
               activebackground="#FF1493", activeforeground="#FFFFFF", font=("Times", 12)).place(x=400, y=460)
        Button(self.root, text="Ввести стоимость", width="20", bg="#DC143C", fg="#FFFFFF", 
               activebackground="#FF1493", activeforeground="#FFFFFF", font=("Times", 12), command=self.price_callback).place(x=285, y=288, anchor="c")
        self.value_option = IntVar()
        self.value_option.set(0)

        Radiobutton(self.root, text="По длине", variable=self.value_option, value=1, bg="#DC143C",
                    activebackground="#FF1493", activeforeground="#FFFFFF", font=("Times", 12)).place(x=225, y=45)
        Radiobutton(self.root, text="По ширине", variable=self.value_option, value=2, bg="#DC143C",
                    activebackground="#FF1493", activeforeground="#FFFFFF", font=("Times", 12)).place(x=225, y=75)
        Radiobutton(self.root, text="По диагонали", variable=self.value_option, value=3, bg="#DC143C",
                    activebackground="#FF1493", activeforeground="#FFFFFF", font=("Times", 12)).place(x=225, y=105)

    def button_action(self):
        try:
            entry_width = float(self.entry_width.get())
            entry_length = float(self.entry_length.get())
            entry_str_l_board = float(self.entry_str_l_board.get())
            entry_str_w_board = float(self.entry_str_w_board.get())
            entry_str_board = int(self.entry_str_board.get())

            if self.value_option.get() == 1:
                result = math.ceil((entry_length * entry_width * 107 / 100) / (
                    (entry_str_l_board * entry_str_w_board * entry_str_board)))
                Label(self.root, text="Количество упаковок: {:d} шт".format(result), width="30", bg="#DC143C",
                      fg="#FFFFFF", font=("Times", 12), justify=LEFT).place(x=190, y=380)
                self.entry_price(result)
            elif self.value_option.get() == 2:
                result = math.ceil((entry_length * entry_width * 110 / 100) / (
                    (entry_str_l_board * entry_str_w_board * entry_str_board)))
                Label(self.root, text="Количество упаковок: {:d} шт".format(result), width="30", bg="#DC143C",
                      fg="#FFFFFF", font=("Times", 12), justify=LEFT).place(x=190, y=380)
                self.entry_price(result)
            elif self.value_option.get() == 3:
                result = math.ceil((entry_length * entry_width * 115 / 100) / (
                    (entry_str_l_board * entry_str_w_board * entry_str_board)))
                Label(self.root, text="Количество упаковок: {:d} шт".format(result), width="30", bg="#DC143C",
                      fg="#FFFFFF", font=("Times", 12), justify=LEFT).place(x=190, y=380)
                self.entry_price(result)
            else:
                messagebox.showinfo('Внимание!', 'Выберите вариант укладки')

        except ValueError:
            messagebox.showerror('Ошибка!', 'Введено неверное значение')

        except AttributeError:
            messagebox.showinfo('Внимание!', 'Заполните все поля')

        except ZeroDivisionError:
            messagebox.showinfo('Внимание!', 'Заполните все поля')

    def entry_price(self, result):
        try:
            if float(self.price.get()) is None:
                messagebox.showinfo('Внимание!', 'Вы не ввели стоимость')
            elif float(self.price.get()) == 0:
                messagebox.showinfo('Внимание!', 'Вы не ввели стоимость')
            else:
                price_result = float(self.price.get()) * result
                Label(self.root, text="Стоимость ламината, рублей: {:.2f}".format(price_result), width="30", bg="#DC143C",
                      fg="#FFFFFF", font=("Times", 12), justify=LEFT).place(x=190, y=405)

        except AttributeError:
            print(" ")