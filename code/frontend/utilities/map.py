import tkinter as tk

def click_coord(event, lbl_coordX, lbl_coordY, canvas_mapa):
    canvas_mapa.delete("marker")
    x, y = event.x, event.y
    x_adjusted = (x / canvas_mapa.winfo_width()) * 200 - 100
    y_adjusted = ((canvas_mapa.winfo_height() - y) / canvas_mapa.winfo_height()) * 200 - 100
    lbl_coordX.config(text=f"X:{x_adjusted:.2f}")
    lbl_coordY.config(text=f"Y:{y_adjusted:.2f}")
    radius = 5
    canvas_mapa.create_oval(x - radius, y - radius, x + radius, y + radius, fill="red", tag="marker")