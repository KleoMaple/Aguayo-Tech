import tkinter as tk

win_order = tk.Tk() ##Cambiar a tk.Toplevel()
win_order.title("Ordenar Productos")
win_order.geometry("900x1000+500+0")
win_order.resizable(height=False, width=False)
img_order = tk.PhotoImage(file="Aguayo-Tech/code/frontend/img/bg_order.png")

canvas_order = tk.Canvas(win_order, width=900, height=1000)
canvas_order.pack(fill="both", expand=True)
canvas_order.create_image(0,0, anchor=tk.NW, image=img_order)


##### FUNCIONES #####
def on_entry_click(event, dato_entry, placeholder):
    if dato_entry.get() == placeholder:
        dato_entry.delete(0, tk.END)
        dato_entry.config(fg='black') 

def on_entry_leave(event, dato_entry, placeholder):
    if dato_entry.get() == "":
        dato_entry.insert(0, placeholder)
        dato_entry.config(fg='grey')

def entry_creator(canvas, x, y, placeholder):
    entry = tk.Entry(win_order, bg="white", fg="gray", font="consolas 14")
    entry.insert(0, placeholder)
    entry.bind('<FocusIn>', lambda event: on_entry_click(event, entry, placeholder))
    entry.bind('<FocusOut>', lambda event: on_entry_leave(event, entry, placeholder))
    window = canvas_order.create_window(x, y, anchor=tk.NW, window=entry)
    return entry

def validar_entradas():
    for entry in entries:
        print(entry.get())

lbl_menu_ord = tk.Label(win_order,
                        text="Ordenar Pedido",
                        font="consolas 22 bold",
                        bg="sky blue",
                        padx=50, pady=20,
                        relief=tk.GROOVE)
lbl_menu_ord.pack(pady=10, padx=10, in_=canvas_order)

###### SELECT Clientes #######

canvas_order.create_text(450,120,
                         text="Seleccione al Cliente Indicado",
                         font="consolas 18 bold")

list_clients = ["Cliente 1","Cliente 2","Cliente 3","Cliente 4","Cliente 5","Cliente 6",
                "Cliente 7","Cliente 8","Cliente 9","Cliente 10","Cliente 11","Cliente 12",]
                #Esta lista debe ser capaz de agarrar los datos del .json con los
                #nombres de cada cliente existente.

selected = tk.StringVar()
selected.set(list_clients[0])

select_clientes = tk.OptionMenu(win_order,selected,*list_clients)
canvas_order.create_window(400,150,anchor=tk.NW,window=select_clientes)

###### FIN DE SELECT #######

#### CAMPOS DE MULTIPLES PRODUCTOS #########

canvas_order.create_text(455,210,
                         text="Ingrese nombre y peso de los productos que desee pedir",
                         font="consolas 16 bold")
canvas_order.create_text(300,260,
                         text="Productos",
                         font="consolas 14 bold")
canvas_order.create_text(600,260,
                         text="Pesos",
                         font="consolas 14 bold")

entries = []
y_increased = 0
for i in range(0,10):
    entry_creator(canvas_order, 205, 290+y_increased, "Producto")
    entry_creator(canvas_order, 505, 290+y_increased, "Peso")
    y_increased = y_increased + 60

win_order.mainloop()