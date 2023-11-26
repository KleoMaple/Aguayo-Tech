import tkinter as tk
from constants import ASSETS_PATH
from frontend.utilities.window import finish_window
from frontend.windows.signup_win import SignUp_win
from frontend.windows.order_win import Order_win
#from frontend.windows.delivered_win import Delivered_win
from frontend.components.button import button

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

img_delivered =tk.PhotoImage(
    file = f"{ASSETS_PATH}bg_delivered.png"
)

canvas = tk.Canvas(main_win, width=700, height=500)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, anchor=tk.NW, image=img_main)


#def get_shipmnet(selected):
 #   Delivered_win(main_win, img_delivered)

lbl_menu_title = tk.Label(main_win,
                          text="MAIN MENU",
                          font="consolas 22 bold",
                          bg="sky blue",
                          padx=100, pady=20,
                          relief=tk.GROOVE, bd=2,
                          width=20)
lbl_menu_title.pack(pady=20, padx=20, in_=canvas)

btn_SignUp = button(
    main_win,
    text="Registrar Cliente",
    command=lambda: SignUp_win(main_win, [img_signup, img_map]),
    font="consolas 22 bold"
)

btn_SignUp.pack(pady=20, padx=20, in_=canvas)

btn_Orders = tk.Button(main_win,
                       text="Realizar Pedidos",
                       font="consolas 22 bold",
                       bg="pale green",
                       relief=tk.GROOVE, bd=2,
                       width=20,
                       activebackground="aquamarine",
                       command=lambda: Order_win(main_win, img_order))
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