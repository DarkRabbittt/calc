import os
from tkinter import *
from tkinter import Entry
import math
from PIL import ImageTk, Image
from tkinter import messagebox
from imgg import InsertImage


class TileWindow:
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
            os.remove("grid_img.png")
        except AttributeError:
            messagebox.showinfo('Внимание!', 'Вы не выбрали изображение')

    def img_label(self):
        try:
            insert = InsertImage()
            self.copy_img = insert.open_img()
            self.pic = Label(self.root, image=self.copy_img)
            self.pic.place(x=415, y=170, anchor="w")
            self.pic_label = Label(self.root, text="Ваша плитка будет выглядеть так:", width="25", bg="#DC143C", fg="#FFFFFF", font=("Times", 12))
            self.pic_label.place(x=415, y=14)
            self.no_image.destroy()
        except AttributeError:
            messagebox.showinfo('Внимание!', 'Вы не выбрали изображение')

    def draw_widgets(self):
        str_length = DoubleVar()
        str_width = DoubleVar()
        str_l_tile = DoubleVar()
        str_w_tile = DoubleVar()

        self.entry_length = Entry(self.root, textvariable=str_length)
        self.entry_width = Entry(self.root, textvariable=str_width)
        self.entry_str_l_tile = Entry(self.root, textvariable=str_l_tile)
        self.entry_str_w_tile = Entry(self.root, textvariable=str_w_tile)

        self.entry_width.place(x=80, y=50, anchor="c")
        self.entry_length.place(x=80, y=100, anchor="c")
        self.entry_str_l_tile.place(x=80, y=150, anchor="c")
        self.entry_str_w_tile.place(x=80, y=200, anchor="c")

        insert = InsertImage()
        self.no_img = insert.no_image()
        self.no_image = Label(self.root, image=self.no_img)
        self.no_image.place(x=415, y=14)

        Label(self.root, text="Длина комнаты, м", width="15", bg="#DC143C", fg="#FFFFFF", font=("Times", 12)).place(x=80, y=25, anchor="c")
        Label(self.root, text="Ширина комнаты, м", width="15", bg="#DC143C", fg="#FFFFFF", font=("Times", 12)).place(x=80, y=75, anchor="c")
        Label(self.root, text="Ширина плитки, cм", width="15", bg="#DC143C", fg="#FFFFFF", font=("Times", 12)).place(x=80, y=125, anchor="c")
        Label(self.root, text="Длина плитки, cм", width="15", bg="#DC143C", fg="#FFFFFF", font=("Times", 12)).place(x=80, y=175, anchor="c")

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

        Radiobutton(self.root, text="Базовый способ", variable=self.value_option, value=1, bg="#DC143C", fg="#000000",
                    activebackground="#FF1493", font=("Times", 12)).place(x=205, y=45)
        Radiobutton(self.root, text="Базовый способ под углом", variable=self.value_option, value=2, bg="#DC143C", fg="#000000",
                    activebackground="#FF1493", font=("Times", 12)).place(x=205, y=75)
        Radiobutton(self.root, text="Шахматы", variable=self.value_option, value=3, bg="#DC143C", fg="#000000",
                    activebackground="#FF1493", font=("Times", 12)).place(x=205, y=105)
        Radiobutton(self.root, text="Шахматы под углом", variable=self.value_option, value=4, bg="#DC143C", fg="#000000",
                    activebackground="#FF1493", font=("Times", 12)).place(x=205, y=135)
        Radiobutton(self.root, text="Укладка со смещением", variable=self.value_option, value=5, bg="#DC143C", fg="#000000",
                    activebackground="#FF1493", font=("Times", 12)).place(x=205, y=165)

    def button_action(self):
        try:
            entry_width = float(self.entry_width.get())
            entry_length = float(self.entry_length.get())
            entry_str_l_tile = float(self.entry_str_l_tile.get())
            entry_str_w_tile = float(self.entry_str_w_tile.get())

            if self.value_option.get() == 1:
                result = math.ceil((entry_length * entry_width) / (
                    (entry_str_l_tile * entry_str_w_tile / 10000)))
                footage = result * (entry_str_w_tile * entry_str_l_tile) / 10000
                Label(self.root, text="Количество плитки: {:d} шт \nМетраж плитки: {:.2f} кв.м".format(result, footage), width="32", bg="#DC143C",
                      fg="#FFFFFF", font=("Times", 12), justify=LEFT).place(x=190, y=380)
                self.entry_price(result)

            elif self.value_option.get() == 2:
                result = math.ceil((entry_length * entry_width) / (
                    (entry_str_l_tile * entry_str_w_tile / 10000)) * 110 / 100)
                footage = result * (entry_str_w_tile * entry_str_l_tile) / 10000
                Label(self.root, text="Количество плитки: {:d} шт \nМетраж плитки: {:.2f} кв.м".format(result, footage),
                      width="32", bg="#DC143C",
                      fg="#FFFFFF", font=("Times", 12), justify=LEFT).place(x=190, y=380)
                self.entry_price(result)

            elif self.value_option.get() == 3:
                result = math.ceil((entry_length * entry_width) /
                                   (entry_str_l_tile * entry_str_w_tile) * 10000)
                r_color = math.ceil(result / 2)
                r_footage = r_color * (entry_str_l_tile * entry_str_w_tile) / 10000
                footage = r_footage * 2
                Label(self.root, text="Количество плитки: {:d} шт \nПлиток каждого цвета: {:d} шт \nМетраж плиток каждого цвета: {:.2f} кв.м \nОбщий метраж плитки: {:.2f} кв.м".format(result, r_color, r_footage, footage),
                      width="32", bg="#DC143C", fg="#FFFFFF", font=("Times", 12), justify=LEFT).place(x=190, y=380)
                self.entry_price(result)

            elif self.value_option.get() == 4:
                result = math.ceil((entry_length * entry_width) /
                                   (entry_str_l_tile * entry_str_w_tile) * 10000)
                r_color = math.ceil(result / 2 * 110 / 100)
                r_footage = r_color * (entry_str_l_tile * entry_str_w_tile) / 10000
                footage = r_footage * 2
                Label(self.root,
                      text="Количество плитки: {:d} шт \nПлиток каждого цвета: {:d} шт \nМетраж плиток каждого цвета: {:.2f} кв.м \nОбщий метраж плитки: {:.2f} кв.м".format(
                          result, r_color, r_footage, footage,),
                      width="32", bg="#DC143C",
                      fg="#FFFFFF", font=("Times", 12), justify=LEFT).place(x=190, y=380)
                self.entry_price(result)

            elif self.value_option.get() == 5:
                result = math.ceil((entry_length * entry_width) /
                                   (entry_str_l_tile * entry_str_w_tile) * 10000)
                r_color = math.ceil(result / 2 * 95 / 100)
                r_footage = r_color * (entry_str_l_tile * entry_str_w_tile) / 10000
                decor = math.ceil(result * 95 / 100)
                footage = r_footage * 2
                Label(self.root,
                      text="Количество плитки: {:d} шт \nПлиток каждого цвета и декоров: {:d} и {:d} шт \nМетраж плиток каждого цвета: {:.2f} кв.м \nОбщий метраж плитки: {:.2f} кв.м".format(
                          result, r_color, decor, r_footage, footage,),
                      width="32", bg="#DC143C",
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
                Label(self.root, text="Стоимость плитки, рублей: {:.2f}".format(price_result), width="30", bg="#DC143C",
                      fg="#FFFFFF", font=("Times", 12), justify=LEFT).place(x=490, y=380)

        except AttributeError:
            print(" ")