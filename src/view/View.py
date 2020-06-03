from tkinter import *


class View:
    def __init__(self, root):
        self.root = root
        self.__font_size = 10
        self.__padding = 5

    def show_message(self, message: str):
        label = Label(
            self.root,
            text=message,
            font=(None, self.__font_size),
            pady=self.__padding,
            padx=self.__padding
        )
        label.pack()
