import tkinter as tk

main_win = tk.Tk()
main_win.title("Interfaz de Usuario")
main_win.geometry("700x500+600+250")
main_win.resizable(width=False, height=False)
img_main = tk.PhotoImage(file="Aguayo-Tech/code/frontend/img/bg_menu.png")
img_signup = tk.PhotoImage(file="Aguayo-Tech/code/frontend/img/bg_signup.png")
img_mapa = tk.PhotoImage(file="Aguayo-Tech/code/frontend/img/img_map.png")

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
    x_adjusted = (x / canvas.winfo_width()) * 200 - 100
    y_adjusted = ((canvas.winfo_height() - y) / canvas.winfo_height()) * 200 - 100
    lbl_coordX.config(text=f"X:{x_adjusted:.2f}")
    lbl_coordY.config(text=f"Y:{y_adjusted:.2f}")
    radius = 5
    canvas_mapa.create_oval(x - radius, y - radius, x + radius, y + radius, fill="red", tag="marker")

###### FIN FUNCIONES #######

##### VENTANA REGISTRO CLIENTES #####
def SignUp_win(main_win):
    main_win.withdraw()
    win_signup = tk.Toplevel()
    win_signup.title("Registro de Clientes")
    win_signup.geometry("900x700+500+200")
    win_signup.resizable(height=False, width=False)
    canvas_signup = tk.Canvas(win_signup, width=900, height=700)
    canvas_signup.pack(fill="both", expand=True)
    canvas_signup.create_image(0,0,anchor=tk.NW, image=img_signup)

    lbl_title_signup = tk.Label(win_signup,
                                text="Registro de Cliente",
                                font="consolas 22 bold",
                                bg="sky blue",
                                padx= 100, pady=20,
                                relief=tk.GROOVE)
    lbl_title_signup.pack(pady=20, padx=20, in_=canvas_signup)

    #### ENTRADA DE NOMBRE Y APELLIDOS ######

    frm_datos = tk.Frame(win_signup, bg="#00a2e8")

    in_nombre = tk.Entry(frm_datos,
                         bg="white", fg="gray",
                         font="consolas 18")
    in_nombre.insert(0, "Nombre")
    in_nombre.bind('<FocusIn>', lambda event: on_entry_click(event, in_nombre, "Nombre"))
    in_nombre.bind('<FocusOut>', lambda event: on_entry_leave(event, in_nombre, "Nombre"))
    in_nombre.pack(padx=5, side=tk.LEFT, in_=frm_datos)

    in_apellido = tk.Entry(frm_datos,
                           bg="white", fg="gray",
                           font="consolas 18")
    in_apellido.insert(0, "Apellido")
    in_apellido.bind('<FocusIn>', lambda event: on_entry_click(event, in_apellido, "Apellido"))
    in_apellido.bind('<FocusOut>', lambda event: on_entry_leave(event, in_apellido, "Apellido"))
    in_apellido.pack(padx=5, side=tk.LEFT, in_=frm_datos)

    frm_datos.pack(in_=canvas_signup)

    lbl_coordx = tk.Label(canvas_signup,
                         bg="white", fg="gray",
                         font="consolas 18",
                         width=8,text="CoordX",
                         relief=tk.GROOVE,
                         bd=3, anchor=tk.W)
    lbl_coordx.place(x=170, y=170)

    lbl_coordy = tk.Label(canvas_signup,
                         bg="white", fg="gray",
                         font="consolas 18",
                         width=8,text="CoordY",
                         relief=tk.GROOVE,
                         bd=3, anchor=tk.W)
    lbl_coordy.place(x=170, y=220)

    ######### FIN DE NOMBRE Y APELLIDOS ########

    ######## MAPA Y COORDENADAS ##############

    canvas_mapa = tk.Canvas(win_signup, width=517, height=440, bg="black")
    canvas_mapa.place(x=285, y=170)
    canvas_mapa.create_image(0,0,anchor=tk.NW, image=img_mapa)
    canvas_mapa.bind("<Button-1>",lambda event: click_coord(event, lbl_coordy, lbl_coordx, canvas_mapa))


    ########### FIN MAPA Y COORDENADAS ########

    btn_end_main = tk.Button(win_signup,
                         text="Salir",
                         font="consolas 14 bold",
                         bg="pale green",
                         relief=tk.GROOVE, bd=2,
                         width=6, height=1,
                         activebackground="aquamarine",
                         command=lambda: finish_window(win_signup, main_win))
    btn_end_main.place(relx=0.475, rely=0.95, in_=canvas_signup, anchor=tk.SW)

######### FIN DE VENTANA REGISTROS ##########

##### VENTANA REALIZACIÓN PEDIDOS #####
def Order_win(main_win):
    main_win.withdraw()
    win_order = tk.Toplevel()
    win_order.title("Realización de Pedidos")
    win_order.geometry("700x500+600+250")
    btn_end_main = tk.Button(win_order,
                         text="Salir",
                         font="consolas 18 bold",
                         bg="pale green",
                         padx=20, pady=20,
                         relief=tk.GROOVE, bd=2,
                         activebackground="aquamarine",
                         command=lambda: finish_window(win_order, main_win))
    btn_end_main.pack(pady=20, padx=20)

########################################

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