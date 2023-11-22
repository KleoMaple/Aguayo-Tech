import tkinter as tk


def finish_window(window, main_win):
    window.destroy()
    if main_win != None:
        main_win.deiconify()