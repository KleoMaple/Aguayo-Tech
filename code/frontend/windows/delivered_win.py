import tkinter as tk
from constants import ASSETS_PATH
from frontend.utilities.window import finish_window



def Delivered_win(main_win, img_delivered):
    main_win.withdraw()
    win_delivered = tk.Toplevel()
    win_delivered.title("Entrega finalizada.")
    win_delivered.geometry("1000x745+500+100")
    win_delivered.resizable(height=False, width=False)
        
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
    #canvas_delivered.create_window(285,0, anchor=tk.NW,window=lbl_title_delivered)    
   
#####  Información CAMIÓN 1 ####      
    canvas_delivered.create_text(500,150,
                             text="Camión 1:",
                             font="consolas 16 bold") 

    combined_info = f"Peso total de entrega: ['pesito'] kg\n" \
                    f"Productos entregados:'productos']\n" \
                    f"Rutas:" 

    lbl_combined_info = tk.Label(win_delivered,
                                 text=combined_info,
                                 font="consola 14 bold",
                                 bg="lavender",
                                 padx=100,
                                 pady=15,
                                 relief=tk.GROOVE)
    lbl_combined_info.pack(pady=60, padx=70, in_=canvas_delivered)


#####  Información CAMIÓN 2 ####      
    canvas_delivered.create_text(500,350,
                             text="Camión 2:",
                             font="consolas 16 bold") 

    combined_info = f"Peso total de entrega: [''] kg\n" \
                    f"Productos entregados:'productos']\n" \
                    f"Rutas: 'rutas'"

    lbl_combined_info = tk.Label(win_delivered,
                                 text=combined_info,
                                 font="consola 14 bold",
                                 bg="lavender",
                                 padx=100,
                                 pady=15,
                                 relief=tk.GROOVE)
    lbl_combined_info.pack(pady=40, padx=70, in_=canvas_delivered)


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
   
