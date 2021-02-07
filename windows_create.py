import random
import string
from tkinter import *
from tkinter import ttk, scrolledtext
from parameters_generator import *


def create_window():
    window = Tk()
    window.title(title_window)
    window.geometry(size_windows)

    label_length_password = Label(window, text=length_password_text)
    label_length_password.place(x=length_password_x, y=length_password_y)

    input_length_password = Entry()
    input_length_password.place(x=entry_password_length_x, y=entry_password_length_y, width=entry_password_length_width)
    input_length_password.focus_set()

    def int_getting():
        getting = input_length_password.get()
        return int(getting)

    checkbox_password_letters = Label(window, text=checkbox_password_letters_text)
    checkbox_password_letters.place(x=checkbox_password_label_letters_x, y=checkbox_password_label_letters_y)

    def pass_generator():
        random_pass = ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in
                               range(int_getting())])
        return random_pass

    def show_new_password():
        pass_result = Text()
        pass_result.insert(END, pass_generator())
        pass_result.yview(END)
        pass_result.configure(state="disabled")
        pass_result.place(x=text_result_x, y=text_result_y, width=text_result_width, height=text_result_height)

    button_password_generator = Button(window, text=text_button, command=show_new_password)
    button_password_generator.place(x=position_button_x, y=position_button_y)

    return window.mainloop()
