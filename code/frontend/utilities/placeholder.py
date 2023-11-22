import tkinter as tk


def on_entry_click(event, dato_entry, placeholder):
    if dato_entry.get() == placeholder:
        dato_entry.delete(0, tk.END)
        dato_entry.config(fg='black') 

def on_entry_leave(event, dato_entry, placeholder):
    if dato_entry.get() == "":
        dato_entry.insert(0, placeholder)
        dato_entry.config(fg='grey')