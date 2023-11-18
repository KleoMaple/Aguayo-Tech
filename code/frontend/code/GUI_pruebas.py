import tkinter as tk

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

### VENTANA REGISTROS CLIENTES ###
win_signup = tk.Tk()
win_signup.title("Registro de Clientes")
win_signup.geometry("900x700+500+200")
img_signup = tk.PhotoImage(file="Aguayo-Tech/code/frontend/img/bg_signup.png")

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

#### FRAME NOMBRE Y APELLIDO CLIENTE ####
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
#########################################


btn_end_main = tk.Button(win_signup,
                         text="Salir",
                         font="consolas 14 bold",
                         bg="pale green",
                         relief=tk.GROOVE, bd=2,
                         width=6, height=1,
                         activebackground="aquamarine",
                         command=lambda: finish_window(win_signup, None))
btn_end_main.pack(pady=20, padx=20, in_=canvas_signup)

win_signup.mainloop()