import tkinter as tk
from constants import ASSETS_PATH
from frontend.utilities.window import finish_window


def Delivered_win(main_win, win_order, route_beyond,route_within):
    main_win.withdraw()
    win_order.destroy()
    win_delivered = tk.Toplevel()
    win_delivered.title("Entrega finalizada.")
    win_delivered.geometry("1000x745+500+100")
    win_delivered.resizable(height=False, width=False)
    global img_delivered
    img_delivered =tk.PhotoImage(file =f"{ASSETS_PATH}bg_delivered.png")
        
    canvas_delivered = tk.Canvas(win_delivered, width=1000, height=500)
    canvas_delivered.pack(fill="both", expand=True)
    canvas_delivered.create_image(0, 0, anchor=tk.NW, image=img_delivered)
    lbl_title_delivered = tk.Label(win_delivered,
                                    text="Envío Realizado",
                                    font="consolas 22 bold",
                                    bg="sky blue",
                                    padx=100,
                                    pady=15,
                                    relief=tk.GROOVE)
    lbl_title_delivered.pack(pady=20, padx=20, in_=canvas_delivered)    
   
#####  Información CAMIÓN 1 ####      
    canvas_delivered.create_text(500,150,
                             text="Camión Pesado:",
                             font="consolas 16 bold") 

    combined_info = f"Peso total de entrega: ['pesito'] kg\n" \
                    f"Productos entregados:'productos']\n" \
                    f"Rutas:" 

    lbl_combined_info1 = tk.Label(win_delivered,
                                 text=route_within,
                                 font="consola 12 bold",
                                 bg="lavender",
                                 padx=50,
                                 relief=tk.GROOVE,
                                 anchor="w", justify="left")
    lbl_combined_info1.place(x=50,y=170)


#####  Información CAMIÓN 2 ####      
    canvas_delivered.create_text(500,350,
                             text="Camión Ligero:",
                             font="consolas 16 bold") 

    lbl_combined_info2 = tk.Label(win_delivered,
                                 text=route_beyond,
                                 font="consola 12 bold",
                                 bg="lavender",
                                 padx=50,
                                 relief=tk.GROOVE,
                                 anchor="w", justify="left")
    lbl_combined_info2.place(x=50,y=370)


### Volver a Menú ###
    btn_back_to_menu = tk.Button(win_delivered,
                                text="Volver al Menú Principal",
                                font="consolas 18 bold",
                                bg="pale green",
                                relief=tk.GROOVE,
                                bd=2,
                                activebackground="aquamarine",
                                command=lambda: finish_window(win_delivered, main_win))
    canvas_delivered.create_window(345, 600, anchor=tk.NW, window=btn_back_to_menu)
    win_delivered.protocol("WM_DELETE_WINDOW", lambda: finish_window(win_delivered, main_win))
   
