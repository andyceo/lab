#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Tkinter Basics.

@see https://pythonprogramming.net/python-3-tkinter-basics-tutorial/
@see https://www.pythonguis.com/faq/which-python-gui-library/

Requirements: Pillow or PIL (sudo apt install python3-pil) and maybe `sudo apt install python3-tk` for Tkinter.
"""
from tkinter import Frame, Tk, Button, BOTH, Menu, Label
from PIL import Image, ImageTk


class Window(Frame):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("GUI")  # changing the title of our master widget
        self.pack(fill=BOTH, expand=1)  # allowing the widget to take the full space of the root window

        # Creating a menu instance
        menu = Menu(master=self.master)
        self.master.config(menu=menu)

        # Create Menu | File instance and add Exit menu item to it
        file = Menu(master=menu)
        menu.add_cascade(label='File', menu=file)
        file.add_command(label='Exit', command=self.client_exit)

        # Create Menu | Edit instance and add Undo, Show Img and Show Text menu items to it
        edit = Menu(master=menu)
        menu.add_cascade(label='Edit', menu=edit)
        edit.add_command(label='Undo')
        edit.add_command(label="Show Img", command=self.show_img)
        edit.add_command(label="Show Text", command=self.show_text)

        quitButton = Button(master=self, text="Quit", command=self.client_exit)  # creating a button instance
        quitButton.place(x=0, y=0)  # placing the button on my window

    def client_exit(self):
        exit()

    def show_img(self):
        load = Image.open("/usr/share/pixmaps/debian-logo.png")
        render = ImageTk.PhotoImage(load)
        img = Label(master=self, image=render)
        img.image = render  # @see https://stackoverflow.com/questions/13148975/tkinter-label-does-not-show-image
        img.place(x=50, y=50)

    def show_text(self):
        text = Label(master=self, text='Hey there good lookin!')
        text.pack()


if __name__ == '__main__':
    root = Tk()  # @see https://stackoverflow.com/questions/53755056/what-is-the-different-between-tk-and-frame
    root.geometry("400x300")  # size of the main window
    app = Window(root)
    root.mainloop()
