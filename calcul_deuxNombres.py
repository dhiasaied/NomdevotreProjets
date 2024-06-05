import tkinter as tk
from tkinter import messagebox

def calculate():
    entry1_text = entry1.get()
    entry2_text = entry2.get()
    
    # Vérification si les entrées sont vides
    if not entry1_text or not entry2_text:
        messagebox.showerror("Erreur", "Veuillez saisir les deux nombres.")
        return
    
    try:
        nombre1 = float(entry1_text)
        nombre2 = float(entry2_text)
        
        somme = nombre1 + nombre2
        produit = nombre1 * nombre2
        moyenne = (nombre1 + nombre2) / 2
        soustraction = nombre1 - nombre2

        result_label.config(text=f"La somme est : {somme}\n"
                                  f"Le produit est : {produit}\n"
                                  f"La moyenne est : {moyenne}\n"
                                  f"La soustraction est : {soustraction}")
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez saisir des nombres valides.")


# Création de la fenêtre
window = tk.Tk()
window.title("Calculatrice")
window.configure(bg="#f0f0f0")

# Setting window dimensions
window.geometry("600x300")

# Styles
label_style = {"font": ("Helvetica", 12)}
entry_style = {"font": ("Helvetica", 12), "bg": "white", "fg": "black", "bd": 2, "relief": "groove"}
button_style = {"font": ("Helvetica", 12), "bg": "#4CAF50", "fg": "white", "activebackground": "#45a049", "bd": 2, "relief": "raised"}
result_style = {"font": ("Helvetica", 12), "bg": "#f0f0f0"}

# Cadre pour l'affichage
result_frame = tk.LabelFrame(window, text="Résultats", bg="#f0f0f0", fg="black")
result_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Entrées pour les nombres
label1 = tk.Label(window, text="Entrez le premier nombre : ", **label_style, bg="#f0f0f0")
label1.grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry1 = tk.Entry(window, **entry_style)
entry1.grid(row=0, column=1, padx=10, pady=5)

label2 = tk.Label(window, text="Entrez le deuxième nombre : ", **label_style, bg="#f0f0f0")
label2.grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry2 = tk.Entry(window, **entry_style)
entry2.grid(row=1, column=1, padx=10, pady=5)

# Bouton de calcul
calculate_button = tk.Button(window, text="Calculer", command=calculate, **button_style)
calculate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

# Résultat
result_label = tk.Label(result_frame, text="", **result_style, justify="left")
result_label.pack()

# Lancement de la boucle principale
window.mainloop()
