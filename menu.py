##
## 3d_python_game
## menu.py
## The menu for selection
##

from tkinter import *

window_menu = Tk()
window_menu.title("3d python game")
window_menu.geometry("1280x720")
window_menu.resizable(False, False)
window_menu.configure(bg="#b9bdb3")

welcome_msg = Label(window_menu, text = "Welcome to my 3d python game", font=('Arial', 40), fg="white", bg="#b9bdb3")
welcome_msg.pack(side = "top", padx = 10, pady=10)

window_menu.mainloop()