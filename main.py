from tkinter import *

window = Tk()
window.config(width=400, height=400, bg="purple")

canvas = Canvas(width=250, height=250, bg="green")
canvas.pack(padx=150, pady=150)

canvas.create_text(125, 125, text="yo world", fill="yellow", font=("Calibiri", 45, "italic"))

window.mainloop()
