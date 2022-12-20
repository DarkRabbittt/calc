import os
from tkinter import *
from tkinter import Entry
import math
from PIL import ImageTk, Image
from tkinter import messagebox
from imgg import InsertImage


class WallpaperWindow:
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

    def width_callback(self, event):
        self.first_option.destroy()
        self.second_option.destroy()
        str_other_width = DoubleVar()
        self.other_width = Entry(self.root, textvariable=str_other_width)
        self.other_width.place(x=285, y=65, anchor="c")

    def length_callback(self, event):
        self.third_option.destroy()
        self.fourth_option.destroy()
        str_other_length = DoubleVar()
        self.other_length = Entry(self.root, textvariable=str_other_length)
        self.other_length.place(x=285, y=165, anchor="c")

    def img_label(self):
        try:
            copy = InsertImage()
            self.copy_img = copy.open_img()
            self.pic = Label(self.root, image=self.copy_img)
            self.pic.place(x=415, y=170, anchor="w")
            self.pic_label = Label(self.root, text="Ваши обои будут выглядеть так:", width="25", bg="#DC143C", fg="#FFFFFF", font=("Times", 12))
            self.pic_label.place(x=415, y=14)
            self.no_image.destroy()
        except AttributeError:
            messagebox.showinfo('Внимание!', 'Вы не выбрали изображение')

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

    def draw_widgets(self):
        str_length = DoubleVar()
        str_height = DoubleVar()
        str_width = DoubleVar()
        str_doors = IntVar()
        str_width_door = DoubleVar()
        str_height_door = DoubleVar()
        str_windows = IntVar()
        str_width_window = DoubleVar()
        str_height_window = DoubleVar()

        insert = InsertImage()
        self.no_img = insert.no_image()
        self.no_image = Label(self.root, image=self.no_img)
        self.no_image.place(x=415, y=14)

        self.entry_length = Entry(self.root, textvariable=str_length)
        self.entry_width = Entry(self.root, textvariable=str_width)
        self.entry_height = Entry(self.root, textvariable=str_height)
        self.entry_doors = Entry(self.root, textvariable=str_doors)
        self.entry_width_door = Entry(self.root, textvariable=str_width_door)
        self.entry_height_door = Entry(self.root, textvariable=str_height_door)
        self.entry_windows = Entry(self.root, textvariable=str_windows)
        self.entry_width_window = Entry(self.root, textvariable=str_width_window)
        self.entry_height_window = Entry(self.root, textvariable=str_height_window)

        self.entry_length.place(x=80, y=50, anchor="c")
        self.entry_width.place(x=80, y=100, anchor="c")
        self.entry_height.place(x=80, y=150, anchor="c")
        self.entry_doors.place(x=80, y=200, anchor="c")
        self.entry_width_door.place(x=80, y=250, anchor="c")
        self.entry_height_door.place(x=80, y=300, anchor="c")
        self.entry_windows.place(x=80, y=350, anchor="c")
        self.entry_width_window.place(x=80, y=400, anchor="c")
        self.entry_height_window.place(x=80, y=450, anchor="c")

        Label(self.root, text="Длина комнаты, м", width="15", bg="#DC143C", fg="#FFFFFF", font=("Times", 12)).place(x=80, y=25, anchor="c")
        Label(self.root, text="Ширина комнаты, м", width="15", bg="#DC143C", fg="#FFFFFF", font=("Times", 12)).place(x=80, y=75, anchor="c")
        Label(self.root, text="Высота комнаты, м", width="15", bg="#DC143C", fg="#FFFFFF", font=("Times", 12)).place(x=80, y=125, anchor="c")
        Label(self.root, text="Количество дверей", width="15", bg="#DC143C", fg="#FFFFFF", font=("Times", 12)).place(x=80, y=175, anchor="c")
        Label(self.root, text="Ширина двери, м", width="15", bg="#DC143C", fg="#FFFFFF", font=("Times", 12)).place(x=80, y=225, anchor="c")
        Label(self.root, text="Высота двери, м", width="15", bg="#DC143C", fg="#FFFFFF", font=("Times", 12)).place(x=80, y=275, anchor="c")
        Label(self.root, text="Количество окон", width="15", bg="#DC143C", fg="#FFFFFF", font=("Times", 12)).place(x=80, y=325, anchor="c")
        Label(self.root, text="Ширина окна, м", width="15", bg="#DC143C", fg="#FFFFFF", font=("Times", 12)).place(x=80, y=375, anchor="c")
        Label(self.root, text="Высота окна, м", width="15", bg="#DC143C", fg="#FFFFFF", font=("Times", 12)).place(x=80, y=425, anchor="c")

        Label(self.root, text="Ширина рулона, м", width="15", bg="#DC143C", fg="#FFFFFF", font=("Times", 12)).place(x=285, y=25, anchor="c")
        Label(self.root, text="Длина рулона, м", width="15", bg="#DC143C", fg="#FFFFFF", font=("Times", 12)).place(x=285, y=120, anchor="c")

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
        self.other_width = Label(self.root, text=r"X", width="2", cursor="hand2", bg="#DC143C", fg="#FFFFFF", font=("Times", 12))
        self.other_width.place(x=365, y=25, anchor="c")
        self.other_width.bind("<Button-1>", self.width_callback)
        self.other_length = Label(self.root, text=r"X", width="2", cursor="hand2", bg="#DC143C", fg="#FFFFFF", font=("Times", 12))
        self.other_length.place(x=365, y=120, anchor="c")
        self.other_length.bind("<Button-1>", self.length_callback)

        self.value_width = IntVar()
        self.value_width.set(0)
        self.value_length = IntVar()
        self.value_length.set(0)
        self.first_option = Radiobutton(self.root, text="0.53 м", variable=self.value_width, value=1, bg="#DC143C", fg="#000000",
                                        activebackground="#FF1493", font=("Times", 12))
        self.first_option.place(x=285, y=55, anchor="c")
        self.second_option = Radiobutton(self.root, text="1.05 м", variable=self.value_width, value=2, bg="#DC143C", fg="#000000",
                                         activebackground="#FF1493", font=("Times", 12))
        self.second_option.place(x=285, y=85, anchor="c")
        self.third_option = Radiobutton(self.root, text="10 м", variable=self.value_length, value=1, bg="#DC143C", fg="#000000",
                                        activebackground="#FF1493", font=("Times", 12))
        self.third_option.place(x=285, y=150, anchor="c")
        self.fourth_option = Radiobutton(self.root, text="25 м", variable=self.value_length, value=2, bg="#DC143C", fg="#000000",
                                         activebackground="#FF1493", font=("Times", 12))
        self.fourth_option.place(x=285, y=180, anchor="c")

    def button_action(self):
        try:
            entry_width = float(self.entry_width.get())
            entry_length = float(self.entry_length.get())
            entry_height = float(self.entry_height.get())
            entry_doors = int(self.entry_doors.get())
            entry_width_door = float(self.entry_width_door.get())
            entry_height_door = float(self.entry_height_door.get())
            entry_windows = int(self.entry_windows.get())
            entry_width_window = float(self.entry_width_window.get())
            entry_height_window = float(self.entry_height_window.get())

            if self.value_width.get() == 1 and self.value_length.get() == 1:
                result = math.ceil((entry_width * (entry_length * 2 + entry_height * 2) - (
                        entry_doors * (entry_width_door * entry_height_door) + (
                           entry_windows * (entry_width_window * entry_height_window)))) / (0.53 * 10))
                Label(self.root, text="Количество рулонов: {:d} шт".format(result), width="30", bg="#DC143C", fg="#FFFFFF", font=("Times", 12), justify=LEFT).place(x=190, y=380)
                self.entry_price(result)

            elif self.value_width.get() == 1 and self.value_length.get() == 2:
                result = math.ceil((entry_width * (entry_length * 2 + entry_height * 2) - (
                        entry_doors * (entry_width_door * entry_height_door) + (
                          entry_windows * (entry_width_window * entry_height_window)))) / (0.53 * 25))
                Label(self.root, text="Количество рулонов: {:d} шт".format(result), width="30", bg="#DC143C", fg="#FFFFFF", font=("Times", 12), justify=LEFT).place(x=190, y=380)
                self.entry_price(result)

            elif self.value_width.get() == 2 and self.value_length.get() == 1:
                result = math.ceil((entry_width * (entry_length * 2 + entry_height * 2) - (
                        entry_doors * (entry_width_door * entry_height_door) + (
                          entry_windows * (entry_width_window * entry_height_window)))) / (1.05 * 10))
                Label(self.root, text="Количество рулонов: {:d} шт".format(result), width="30", bg="#DC143C", fg="#FFFFFF", font=("Times", 12), justify=LEFT).place(x=190, y=380)
                self.entry_price(result)

            elif self.value_width.get() == 2 and self.value_length.get() == 2:
                result = math.ceil((entry_width * (entry_length * 2 + entry_height * 2) - (
                        entry_doors * (entry_width_door * entry_height_door) + (
                          entry_windows * (entry_width_window * entry_height_window)))) / (1.05 * 25))
                Label(self.root, text="Количество рулонов: {:d} шт".format(result), width="30", bg="#DC143C", fg="#FFFFFF", font=("Times", 12), justify=LEFT).place(x=190, y=380)
                self.entry_price(result)

            elif (float(self.other_width.get())) != None and self.value_length.get() == 1:
                result = math.ceil((entry_width * (entry_length * 2 + entry_height * 2) - (
                        entry_doors * (entry_width_door * entry_height_door) + (
                          entry_windows * (entry_width_window * entry_height_window)))) / (
                                           float(self.other_width.get()) * 10))
                Label(self.root, text="Количество рулонов: {:d} шт".format(result), width="30", bg="#DC143C", fg="#FFFFFF", font=("Times", 12), justify=LEFT).place(x=190, y=380)
                self.entry_price(result)

            elif (float(self.other_width.get())) != None and self.value_length.get() == 2:
                result = math.ceil((entry_width * (entry_length * 2 + entry_height * 2) - (
                        entry_doors * (entry_width_door * entry_height_door) + (
                          entry_windows * (entry_width_window * entry_height_window)))) / (
                                           float(self.other_width.get()) * 25))
                Label(self.root, text="Количество рулонов: {:d} шт".format(result), width="30", bg="#DC143C", fg="#FFFFFF", font=("Times", 12), justify=LEFT).place(x=190, y=380)
                self.entry_price(result)

            elif self.value_width.get() == 1 and ((float(self.other_length.get())) != None):
                result = math.ceil((entry_width * (entry_length * 2 + entry_height * 2) - (
                        entry_doors * (entry_width_door * entry_height_door) + (
                          entry_windows * (entry_width_window * entry_height_window)))) / (
                                           0.53 * (float(self.other_length.get()))))
                Label(self.root, text="Количество рулонов: {:d} шт".format(result), width="30", bg="#DC143C", fg="#FFFFFF", font=("Times", 12), justify=LEFT).place(x=190, y=380)
                self.entry_price(result)

            elif self.value_width.get() == 2 and ((float(self.other_length.get())) != None):
                result = math.ceil((entry_width * (entry_length * 2 + entry_height * 2) - (
                        entry_doors * (entry_width_door * entry_height_door) + (
                          entry_windows * (entry_width_window * entry_height_window)))) / (
                                           1.05 * (float(self.other_length.get()))))
                Label(self.root, text="Количество рулонов: {:d} шт".format(result), width="30", bg="#DC143C", fg="#FFFFFF", font=("Times", 12), justify=LEFT).place(x=190, y=380)
                self.entry_price(result)

            elif (float(self.other_width.get())) != None and (float(self.other_length.get())) != None:
                result = math.ceil((entry_width * (entry_length * 2 + entry_height * 2) - (
                        entry_doors * (entry_width_door * entry_height_door) + (
                           entry_windows * (entry_width_window * entry_height_window)))) / (
                                           float(self.other_width.get()) * (float(self.other_length.get()))))
                Label(self.root, text="Количество рулонов: {:d} шт".format(result), width="30", bg="#DC143C", fg="#FFFFFF", font=("Times", 12), justify=LEFT).place(x=190, y=380)
                self.entry_price(result)

            else:
                messagebox.showinfo('Внимание!', 'Выберите длину и ширину рулона')

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
                Label(self.root, text="Стоимость обоев, рублей: {:.2f}".format(price_result), width="30", bg="#DC143C", fg="#FFFFFF", font=("Times", 12), justify=LEFT).place(x=190, y=405)

        except AttributeError:
            print(" ")