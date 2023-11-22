import tkinter as tk
from constants import ASSETS_PATH

from services.clients import get_clients_names, get_clients

from frontend.components.button import button

from frontend.utilities.placeholder import on_entry_click, on_entry_leave
from frontend.utilities.window import finish_window

from frontend.windows.signup_win import SignUp_win

main_win = tk.Tk()
main_win.title("Interfaz de Usuario")
main_win.geometry("700x500+600+250")
main_win.resizable(width = False, height = False)

img_main = tk.PhotoImage(
    file=f"{ASSETS_PATH}bg_menu.png"
)
img_signup = tk.PhotoImage(
    file = f"{ASSETS_PATH}bg_signup.png"
)

img_map = tk.PhotoImage(
    file = f"{ASSETS_PATH}img_map.png"
)

img_order = tk.PhotoImage(
    file = f"{ASSETS_PATH}bg_order.png"
)

canvas = tk.Canvas(main_win, width=700, height=500)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, anchor=tk.NW, image=img_main)


##### FUNCIONES #####

def entry_creator(canvas, x, y, placeholder, win_order, canvas_order):
    entry = tk.Entry(win_order, bg="white", fg="gray", font="consolas 14")
    entry.insert(0, placeholder)
    entry.bind('<FocusIn>', lambda event: on_entry_click(event, entry, placeholder))
    entry.bind('<FocusOut>', lambda event: on_entry_leave(event, entry, placeholder))
    canvas_order.create_window(x, y, anchor=tk.NW, window=entry)
    return entry

###### FIN FUNCIONES #######

##### VENTANA REALIZACIÓN PEDIDOS #####
def Order_win(main_win):
    main_win.withdraw()
    win_order = tk.Toplevel()
    win_order.title("Realización de Pedidos")
    win_order.geometry("900x1000+500+0")
    win_order.resizable(height=False, width=False)

    canvas_order = tk.Canvas(win_order, width=900, height=1000)
    canvas_order.pack(fill="both", expand=True)
    canvas_order.create_image(0,0, anchor=tk.NW, image=img_order)

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
       
    clients = get_clients()

    list_clients = get_clients_names(clients)
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
        entry_creator(canvas_order, 205, 290+y_increased, "Producto",win_order,canvas_order)
        entry_creator(canvas_order, 505, 290+y_increased, "Peso",win_order,canvas_order)
        y_increased = y_increased + 60

    btn_end_main = tk.Button(win_order,
                         text="Salir",
                         font="consolas 18 bold",
                         bg="pale green",
                         relief=tk.GROOVE, bd=2,
                         activebackground="aquamarine",
                         command=lambda: finish_window(win_order, main_win))
    canvas_order.create_window(200,900, anchor=tk.NW,window=btn_end_main)

    btn_confirm_purchase = tk.Button(win_order,text="Confirmar Compra",
                                     font="consolas 18 bold",
                                     bg="pale green",
                                     relief=tk.GROOVE,
                                     bd=2,activebackground="aquamarine",
                                     #command=#Realizar funcion
                                     )
    canvas_order.create_window(300,900, anchor=tk.NW,window=btn_confirm_purchase)

    btn_add_more_products = tk.Button(win_order,text="Más Productos",
                                     font="consolas 18 bold",
                                     bg="pale green",
                                     relief=tk.GROOVE,
                                     bd=2,activebackground="aquamarine",
                                     #command=#Realizar funcion
                                     )
    canvas_order.create_window(545,900, anchor=tk.NW,window=btn_add_more_products)
    
######### FIN DE VENTANA PEDIDOS/ORDENES ##########

##### BOTONES DE MENU INICIO ######
lbl_menu_title = tk.Label(main_win,
                          text="MAIN MENU",
                          font="consolas 22 bold",
                          bg="sky blue",
                          padx=100, pady=20,
                          relief=tk.GROOVE, bd=2,
                          width=20)
lbl_menu_title.pack(pady=20, padx=20, in_=canvas)

btn_SignUp = tk.Button(main_win,
                       text="Registrar Cliente",
                       font="consolas 22 bold",
                       bg="pale green",
                       relief=tk.GROOVE, bd=2,
                       width=20,
                       activebackground="aquamarine",
                       command=lambda: SignUp_win(main_win, [img_signup, img_map]))
btn_SignUp.pack(pady=20, padx=20, in_=canvas)

btn_Orders = tk.Button(main_win,
                       text="Realizar Pedidos",
                       font="consolas 22 bold",
                       bg="pale green",
                       relief=tk.GROOVE, bd=2,
                       width=20,
                       activebackground="aquamarine",
                       command=lambda: Order_win(main_win))
btn_Orders.pack(pady=20, padx=20, in_=canvas)

btn_end_main = tk.Button(main_win,
                         text="Salir",
                         font="consolas 18 bold",
                         bg="pale green",
                         relief=tk.GROOVE, bd=2,
                         activebackground="aquamarine",
                         command=lambda: finish_window(main_win, None))
btn_end_main.pack(pady=20, padx=20, in_=canvas)

main_win.mainloop()