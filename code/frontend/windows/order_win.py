import json
import tkinter as tk
from services.clients import get_clients_names, get_clients
from frontend.utilities.placeholder import on_entry_click, on_entry_leave
from frontend.utilities.window import finish_window
from constants import CLIENTS_PATH, ORDERS_PATH

def coordinates_client(nombre, apellido, data):
    for client in data['clients']:
        if client['nombre'] == nombre and client['apellido'] == apellido:
            return client['coordenada_X'], client['coordenada_Y']
    return None, None

def validar_entradas(entries, selected, orders, lbl_message_products):
    user = selected.get()
    producto_tmp = ""
    peso_tmp = ""
    products = []
    peso_sum = 0
    ban = 0
    reset = 0
    for entry in entries:
        if reset == 1:
            reset = 0
            producto_tmp = ""
            peso_tmp = ""
        if ban == 0:
            if entry.get() == "Producto":
                ban += 1
                continue
            else:
                producto_tmp = entry.get()
                ban += 1
        else:
            if entry.get() == "Peso":
                reset = 1
                ban -= 1
                continue
            else:
                peso_tmp = entry.get()
                ban -= 1
                reset = 1
        if producto_tmp != "" and peso_tmp != "":
            products.append(producto_tmp)
            peso_sum = peso_sum + float(peso_tmp)

    ###OBTENER COORDENADAS DEL CLIENTE   
    nombre, apellido = user.split()
    with open(CLIENTS_PATH, 'r', encoding="UTF-8") as file:
        data = json.load(file)
    coord_x, coord_y = coordinates_client(nombre, apellido, data)
    existing_client = any(client[0] == user for client in orders)
    if len(products) > 0:
        if existing_client:
            for clients in orders:
                if clients[0] == user:
                    for product in products:
                        clients[1].append(product)
                    clients[2] = clients[2] + peso_sum
                    break
            lbl_message_products.config(text="Productos Añadidos")
            lbl_message_products.after(5000, lambda: lbl_message_products.config(text=""))
        else:        
            orders.append([user, products, peso_sum, coord_x, coord_y])
            lbl_message_products.config(text="Productos Añadidos")
            lbl_message_products.after(5000, lambda: lbl_message_products.config(text=""))
    

def entry_creator(x, y, placeholder, win_order, canvas_order):
    entry = tk.Entry(win_order, bg="white", fg="gray", font="consolas 14")
    entry.insert(0, placeholder)
    entry.bind('<FocusIn>', lambda event: on_entry_click(event, entry, placeholder))
    entry.bind('<FocusOut>', lambda event: on_entry_leave(event, entry, placeholder))
    canvas_order.create_window(x, y, anchor=tk.NW, window=entry)
    return entry


def confirm_products(entries, selected, orders, lbl_message_products):
    validar_entradas(entries, selected, orders, lbl_message_products)
    ####SUBIR TODOS LOS DATOS AL ALGORITMO DE RUTAS
    #LA LISTA QUE DEVUELVE TIENE LA SIGUIENTE ESTRUCTURA 
    #["CLIENTE, [PRODUCTOS], TOTAL_PESOS, COORD_X, COORD_Y"]
    
    if len(orders) != 0:
        with open(ORDERS_PATH, 'r', encoding="UTF-8") as file:
            data = json.load(file)
        for value in orders:
            nombre, apellido = value[0].split()
            new_order = {
                "client":{
                    "nombre": nombre,
                    "apellido": apellido,
                    "coordenada_X": value[3],
                    "coordenada_Y": value[4]
                },
                "product":{
                    "nombre": value[1],
                    "peso": value[2]
                }
            }
            data["orders"].append(new_order)
            with open(ORDERS_PATH, 'w', encoding="UTF-8") as file:
                json.dump(data,file,indent=4)
        lbl_message_products.config(text="Pedido Registrado")
        lbl_message_products.after(5000, lambda: lbl_message_products.config(text=""))
    orders.clear()

def add_more_products(entries, selected, orders, lbl_message_products):
    validar_entradas(entries, selected, orders, lbl_message_products)
    for i, entry in enumerate(entries):
        if i%2 == 0:
            entry.delete(0, tk.END)
            entry.insert(0, "Producto")
            entry.config(fg="gray")
        else:
            entry.delete(0, tk.END)
            entry.insert(0, "Peso")
            entry.config(fg="gray")

def Order_win(main_win, img_order):
    with open(ORDERS_PATH, 'r') as file:
        data = json.load(file)
    data["orders"] = []
    with open(ORDERS_PATH, 'w') as file:
        json.dump(data, file, indent=4)
    main_win.withdraw()
    win_order = tk.Toplevel()
    win_order.title("Realización de Pedidos")
    win_order.geometry("900x700+500+150")
    win_order.resizable(height=False, width=False)

    canvas_order = tk.Canvas(win_order, width=900, height=1000)
    canvas_order.pack(side="left", fill="both", expand=True)

    canvas_order.create_image(0,0, anchor=tk.NW, image=img_order)
    lbl_menu_ord = tk.Label(win_order,
                            text="Ordenar Pedido",
                            font="consolas 22 bold",
                            bg="sky blue",
                            padx=50, pady=20,
                            relief=tk.GROOVE)
    canvas_order.create_window(285,0, anchor=tk.NW,window=lbl_menu_ord)

    ###### SELECT Clientes #######

    canvas_order.create_text(450,120,
                             text="Seleccione al Cliente Indicado",
                             font="consolas 18 bold")
       
    clients = get_clients()
    list_clients = get_clients_names(clients)

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
    orders = []
    y_increased = 0
    for i in range(0,4):
        entry_producto = entry_creator(205, 290+y_increased, "Producto",win_order,canvas_order)
        entry_peso = entry_creator(505, 290+y_increased, "Peso",win_order,canvas_order)
        entries.append(entry_producto)
        entries.append(entry_peso)
        y_increased = y_increased + 60

    lbl_message_products = tk.Label(canvas_order,
                                    text="",
                                    font="consolas 14 bold",
                                    width=25,
                                    relief=tk.GROOVE,
                                    bd=3)
    lbl_message_products.place(x=325, y=650)

    btn_end_main = tk.Button(win_order,
                         text="Salir",
                         font="consolas 18 bold",
                         bg="pale green",
                         relief=tk.GROOVE, bd=2,
                         activebackground="aquamarine",
                         command=lambda: finish_window(win_order, main_win))
    canvas_order.create_window(200,550, anchor=tk.NW,window=btn_end_main)

    btn_confirm_purchase = tk.Button(win_order,text="Confirmar Pedido",
                                     font="consolas 18 bold",
                                     bg="pale green",
                                     relief=tk.GROOVE,
                                     bd=2,activebackground="aquamarine",
                                     command=lambda:confirm_products(entries, selected, orders, lbl_message_products)
                                     )
    canvas_order.create_window(300,550, anchor=tk.NW,window=btn_confirm_purchase)

    btn_add_more_products = tk.Button(win_order,text="Más Productos",
                                     font="consolas 18 bold",
                                     bg="pale green",
                                     relief=tk.GROOVE,
                                     bd=2,activebackground="aquamarine",
                                     command=lambda: add_more_products(entries, selected, orders, lbl_message_products)
                                     )
    canvas_order.create_window(545,550, anchor=tk.NW,window=btn_add_more_products)
    win_order.protocol("WM_DELETE_WINDOW", lambda: finish_window(win_order, main_win))