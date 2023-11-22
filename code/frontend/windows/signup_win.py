import tkinter as tk

from frontend.components.button import button

from frontend.utilities.placeholder import on_entry_click, on_entry_leave
from frontend.utilities.window import finish_window

from frontend.utilities.map import click_coord

def hola():
    print("Hola")

def SignUp_win(main_win, images):
    main_win.withdraw()
    win_signup = tk.Toplevel()
    win_signup.title("Registro de Clientes")
    win_signup.geometry("1000x800+500+100")
    win_signup.resizable(height=False, width=False)
    canvas_signup = tk.Canvas(win_signup, width=900, height=700)
    canvas_signup.pack(fill="both", expand=True)
    canvas_signup.create_image(0,0,anchor=tk.NW, image=images[0])

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
    canvas_mapa.create_image(0,0,anchor=tk.NW, image=images[1])
    canvas_mapa.bind("<Button-1>",lambda event: click_coord(event, lbl_coordy, lbl_coordx, canvas_mapa))


    ########### FIN MAPA Y COORDENADAS ########

    btn_registrar = button(win_signup, "Registrar", lambda: hola())
    
    canvas_signup.create_window(175,420,anchor=tk.NW,window = btn_registrar)

    btn_end_main = button(win_signup, "Salir", lambda: finish_window(win_signup, main_win))

    canvas_signup.create_window(175,490,anchor=tk.NW,window=btn_end_main)