import tkinter as tk

main_win = tk.Tk()
main_win.title("Interfaz de Usuario")
main_win.geometry("700x500+600+250")
main_win.resizable(width=False, height=False)
imagen_tkinter = tk.PhotoImage(file="frontend/img/bg_menu.png")

canvas = tk.Canvas(main_win, width=700, height=500)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, anchor=tk.NW, image=imagen_tkinter)


##### FUNCIONES BORRAR VENTANAS #####
def finish_window(window, main_win):
    window.destroy()
    if main_win != None:
        main_win.deiconify()

##### VENTANA REGISTRO CLIENTES #####
def SignUp_win(main_win):
    main_win.withdraw()
    win_signup = tk.Toplevel()
    win_signup.title("Registro de Clientes")
    win_signup.geometry("700x500+600+250")
    btn_end_main = tk.Button(win_signup,
                         text="Salir",
                         font="consolas 18 bold",
                         bg="pale green",
                         padx=20, pady=20,
                         relief=tk.GROOVE, bd=2,
                         activebackground="aquamarine",
                         command=lambda: finish_window(win_signup, main_win))
    btn_end_main.pack(pady=20, padx=20)

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
                       padx=20, pady=20,
                       relief=tk.GROOVE, bd=2,
                       width=15,
                       activebackground="aquamarine",
                       command=lambda: SignUp_win(main_win))
btn_SignUp.pack(pady=20, padx=20, in_=canvas)

btn_Orders = tk.Button(main_win,
                       text="Realizar Pedidos",
                       font="consolas 22 bold",
                       bg="pale green",
                       padx=20, pady=20,
                       relief=tk.GROOVE, bd=2,
                       width=15,
                       activebackground="aquamarine",
                       command=lambda: Order_win(main_win))
btn_Orders.pack(pady=20, padx=20, in_=canvas)

btn_end_main = tk.Button(main_win,
                         text="Salir",
                         font="consolas 18 bold",
                         bg="pale green",
                         padx=20, pady=20,
                         relief=tk.GROOVE, bd=2,
                         activebackground="aquamarine",
                         command=lambda: finish_window(main_win, None))
btn_end_main.pack(pady=20, padx=20, in_=canvas)
