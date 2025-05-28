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

welcome_msg = Label(window_menu, text = "Welcome to my 3d python game", font=("Helvetica", 60), fg="white", bg="#b9bdb3")
welcome_msg.pack(side = "top", padx = 10, pady=50)

new_game_button = Button(window_menu, text = "New game", font=("Comic Sans Ms", 60), fg="white", bg="#59534e", width = 20)
new_game_button.pack(side= "top", padx=30, pady=10)

load_game_button = Button(window_menu, text = "Load game", font=("Comic Sans Ms", 60), fg="white", bg="#59534e", width = 20)
load_game_button.pack(side= "top", padx=30, pady=10)

other_button = Button(window_menu, text = "Other", font=("Comic Sans Ms", 60), fg="white", bg="#59534e", width = 20)
other_button.pack(side= "top", padx=30, pady=10)

quit_button = Button(window_menu, text = "Quit", font=("Comic Sans Ms", 60), fg="white", bg="#59534e", width = 20, command=window_menu.destroy)
quit_button.pack(side= "top", padx=30, pady=10)

window_menu.mainloop()