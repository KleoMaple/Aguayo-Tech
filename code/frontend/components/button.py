import tkinter as tk

from typing import Callable

def button(
        window,
        text: str,
        command: Callable[[], None],
        font: str = "consolas 14 bold",
        bg: str = "pale green",
        activebackground="aquamarine"

    ) -> tk.Button:
    """
        Crea un botón con el texto y la función que se le pase como parámetro
    """
    return tk.Button(
        window,
        text = text,
        command = command,
        font = font,
        bg = bg,
        relief = tk.GROOVE,
        bd = 2,
        padx=10,
        pady=5,
        activebackground = activebackground
    )
    