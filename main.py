##
## 3d_python_game
## menu.py
## Menu FPS Post-Apocalyptique - Centrale Nucléaire
##

from tkinter import *
from tkinter import messagebox
import sys

def check_screen_size():
    """Vérifie si l'écran est assez grand pour le jeu"""
    root_temp = Tk()
    root_temp.withdraw()
    screen_width = root_temp.winfo_screenwidth()
    screen_height = root_temp.winfo_screenheight()
    root_temp.destroy()
    if screen_width < 1280 or screen_height < 720:
        messagebox.showerror("Écran trop petit", f"Écran pas assez grand!\nRésolution requise: 1280x720\nVotre résolution: {screen_width}x{screen_height}")
        sys.exit()

def new_game():
    print("Mission: Récupération du plan ultime...")
    # Lancer le jeu principal

def load_game():
    print("Chargement de la mission en cours...")
    # Charger une partie sauvegardée

def options():
    print("Configuration des équipements...")
    # Menu des options/paramètres

def quit_game():
    if messagebox.askquestion("Abandonner la Mission", "Abandonner la mission de sauvetage?") == "yes":
        window_menu.destroy()

# Vérification écran et création fenêtre
check_screen_size()
window_menu = Tk()
window_menu.title("NUCLEAR UNDERGROUND - Mission Critique")
window_menu.geometry("1280x720")
window_menu.resizable(False, False)
window_menu.configure(bg="#0a0a0a")  # Noir profond

# Centrer la fenêtre
window_menu.update_idletasks()
x = (window_menu.winfo_screenwidth() // 2) - (1280 // 2)
y = (window_menu.winfo_screenheight() // 2) - (720 // 2)
window_menu.geometry(f"1280x720+{x}+{y}")

# Titre principal avec effet radioactif
title_frame = Frame(window_menu, bg="#0a0a0a")
title_frame.pack(pady=(60, 20))

title_main = Label(title_frame, text="☢ NUCLEAR UNDERGROUND ☢", font=("Courier New", 36, "bold"), fg="#00ff00", bg="#0a0a0a")
title_main.pack()

subtitle = Label(title_frame, text="MISSION CRITIQUE - RÉCUPÉRATION DU PLAN ULTIME", font=("Courier New", 14, "bold"), fg="#ff6600", bg="#0a0a0a")
subtitle.pack(pady=(10, 0))

# Texte d'ambiance
lore_text = Label(window_menu, text="Les sous-sols irradiés vous attendent...\nDes créatures mutantes rôdent dans l'ombre.\nSeul le plan ultime peut stopper la catastrophe.", font=("Courier New", 12), fg="#cccccc", bg="#0a0a0a", justify=CENTER)
lore_text.pack(pady=(20, 40))

# Style des boutons post-apocalyptique
button_style = {"font": ("Courier New", 18, "bold"), "fg": "#00ff00", "bg": "#1a1a1a", "activebackground": "#ff6600", "activeforeground": "#000000", "width": 20, "height": 2, "relief": "raised", "bd": 3, "cursor": "crosshair"}

# Boutons du menu
new_game_button = Button(window_menu, text="► NOUVELLE MISSION", command=new_game, **button_style)
new_game_button.pack(pady=12)

load_game_button = Button(window_menu, text="► REPRENDRE MISSION", command=load_game, **button_style)
load_game_button.pack(pady=12)

options_button = Button(window_menu, text="► ÉQUIPEMENTS", command=options, **button_style)
options_button.pack(pady=12)

quit_button = Button(window_menu, text="► ABANDONNER", command=quit_game, **button_style)
quit_button.pack(pady=12)

# Effets hover radioactifs
def on_enter(event):
    event.widget.config(bg="#ff6600", fg="#000000")

def on_leave(event):
    event.widget.config(bg="#1a1a1a", fg="#00ff00")

# Appliquer les effets
for button in [new_game_button, load_game_button, options_button, quit_button]:
    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)

# Avertissement en bas
warning = Label(window_menu, text="⚠ ZONE CONTAMINÉE - AUTORISATION NIVEAU 5 REQUISE ⚠", font=("Courier New", 10, "bold"), fg="#ff0000", bg="#0a0a0a")
warning.pack(side=BOTTOM, pady=20)

window_menu.mainloop()