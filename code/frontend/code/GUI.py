import tkinter as tk
from constants import ASSETS_PATH

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
img_mapa = tk.PhotoImage(
    file = f"{ASSETS_PATH}img_map.png"
)
img_order = tk.PhotoImage(
    file = f"{ASSETS_PATH}bg_order.png"
)

canvas = tk.Canvas(main_win, width=700, height=500)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, anchor=tk.NW, image=img_main)


##### FUNCIONES #####
def finish_window(window, main_win):
    window.destroy()
    if main_win != None:
        main_win.deiconify()

def on_entry_click(event, dato_entry, placeholder):
    if dato_entry.get() == placeholder:
        dato_entry.delete(0, tk.END)
        dato_entry.config(fg='black') 

def on_entry_leave(event, dato_entry, placeholder):
    if dato_entry.get() == "":
        dato_entry.insert(0, placeholder)
        dato_entry.config(fg='grey')

def click_coord(event, lbl_coordX, lbl_coordY, canvas_mapa):
    canvas_mapa.delete("marker")
    x, y = event.x, event.y
    x_adjusted = (x / canvas_mapa.winfo_width()) * 200 - 100
    y_adjusted = ((canvas_mapa.winfo_height() - y) / canvas_mapa.winfo_height()) * 200 - 100
    lbl_coordX.config(text=f"X:{x_adjusted:.2f}")
    lbl_coordY.config(text=f"Y:{y_adjusted:.2f}")
    radius = 5
    canvas_mapa.create_oval(x - radius, y - radius, x + radius, y + radius, fill="red", tag="marker")

def entry_creator(canvas, x, y, placeholder, win_order, canvas_order):
    entry = tk.Entry(win_order, bg="white", fg="gray", font="consolas 14")
    entry.insert(0, placeholder)
    entry.bind('<FocusIn>', lambda event: on_entry_click(event, entry, placeholder))
    entry.bind('<FocusOut>', lambda event: on_entry_leave(event, entry, placeholder))
    canvas_order.create_window(x, y, anchor=tk.NW, window=entry)
    return entry

###### FIN FUNCIONES #######

##### VENTANA REGISTRO CLIENTES #####
def SignUp_win(main_win):
    main_win.withdraw()
    win_signup = tk.Toplevel()
    win_signup.title("Registro de Clientes")
    win_signup.geometry("1000x800+500+100")
    win_signup.resizable(height=False, width=False)
    canvas_signup = tk.Canvas(win_signup, width=900, height=700)
    canvas_signup.pack(fill="both", expand=True)
    canvas_signup.create_image(0,0,anchor=tk.NW, image=img_signup)

    lbl_title_signup = tk.Label(win_signup,
                                text="Registro de Cliente",
                                font="consolas 22 bold",
                                bg="sky blue",
                                padx=100, pady=20,
                                relief=tk.GROOVE)
    lbl_title_signup.pack(pady=20, padx=20, in_=canvas_signup)

    #### ENTRADA DE NOMBRE Y APELLIDOS ######

    in_nombre = tk.Entry(win_signup,
                         bg="white",fg="gray",
                         font="consolas 18",
                         relief=tk.GROOVE)
    in_nombre.insert(0, "Nombre")
    in_nombre.bind('<FocusIn>', lambda event: on_entry_click(event, in_nombre, "Nombre"))
    in_nombre.bind('<FocusOut>', lambda event: on_entry_leave(event, in_nombre, "Nombre"))
    canvas_signup.create_window(220,115,anchor=tk.NW,window=in_nombre)

    in_apellido = tk.Entry(win_signup,
                           bg="white", fg="gray",
                           font="consolas 18",
                           relief=tk.GROOVE)
    in_apellido.insert(0, "Apellido")
    in_apellido.bind('<FocusIn>', lambda event: on_entry_click(event, in_apellido, "Apellido"))
    in_apellido.bind('<FocusOut>', lambda event: on_entry_leave(event, in_apellido, "Apellido"))
    canvas_signup.create_window(500,115,anchor=tk.NW,window=in_apellido)
    canvas_signup.create_text(485,160,text="Ingresar datos de nuevo cliente", font="consolas 16 bold")

    lbl_coordx = tk.Label(canvas_signup,
                         bg="white", fg="gray",
                         font="consolas 18",
                         width=8,text="Coord Y",
                         relief=tk.GROOVE,
                         bd=3, anchor=tk.W)
    lbl_coordx.place(x=250, y=260)

    lbl_coordy = tk.Label(canvas_signup,
                         bg="white", fg="gray",
                         font="consolas 18",
                         width=8,text="Coord X",
                         relief=tk.GROOVE,
                         bd=3, anchor=tk.W)
    lbl_coordy.place(x=100, y=260)
    canvas_signup.create_text(210,350,text="Haga Click en el Mapa para seleccionar\nla dirección de entrega.",
                              font="consolas 14 bold",anchor=tk.CENTER)

    ######### FIN DE NOMBRE Y APELLIDOS ########

    ######## MAPA Y COORDENADAS ##############

    canvas_mapa = tk.Canvas(win_signup, width=517, height=440, bg="black")
    canvas_mapa.place(x=415, y=220)
    canvas_mapa.create_image(0,0,anchor=tk.NW, image=img_mapa)
    canvas_mapa.bind("<Button-1>",lambda event: click_coord(event, lbl_coordy, lbl_coordx, canvas_mapa))


    ########### FIN MAPA Y COORDENADAS ########

    btn_register = tk.Button(win_signup,
                             text="Registrar",
                             font="consolas 14 bold",
                             bg="pale green",
                             relief=tk.GROOVE, bd=2,
                             width=10, height=1,
                             activebackground="aquamarine")
                             #command=lambda: finish_window(win_signup, main_win))
    canvas_signup.create_window(175,420,anchor=tk.NW,window=btn_register)

    btn_end_main = tk.Button(win_signup,
                             text="Salir",
                             font="consolas 14 bold",
                             bg="pale green",
                             relief=tk.GROOVE, bd=2,
                             width=10, height=1,
                             activebackground="aquamarine",
                             command=lambda: finish_window(win_signup, main_win))
    canvas_signup.create_window(175,490,anchor=tk.NW,window=btn_end_main)

######### FIN DE VENTANA REGISTROS ##########

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
                       command=lambda: SignUp_win(main_win))
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