import tkinter as tk

def saisie():
    n = 0
    while not (1 <= n <= 9):
        n = int(input("Donnez le nombre de cases des tableaux (1 < n < 9): "))
    return n

def afficher(n):
    text = ""
    for i in range(1, 10):
        text += f"{n} X {i} = {n*i}\n"
    return text

def on_button_click():
    n = int(entry.get())
    output_text = afficher(n)
    output_label.config(text=output_text)

window = tk.Tk()
window.title("Table de multiplication")

window.geometry("400x400")

window.configure(bg="#f0f0f0")

# Style
font_style = ("Arial", 12)
bg_color = "#f0f0f0"
button_color = "#4CAF50"
button_fg_color = "white"
entry_bg_color = "white"
output_bg_color = "#E0E0E0"
output_font_style = ("Arial", 11)

entry_label = tk.Label(window, text="Entrez un nombre (1 < n < 9):", bg=bg_color, font=font_style)
entry_label.pack(pady=(20, 5))

entry = tk.Entry(window, bg=entry_bg_color)
entry.pack(pady=5)

button_style = {
    "bg": button_color,
    "fg": button_fg_color,
    "font": font_style,
    "padx": 10,
    "pady": 5,
    "borderwidth": 0,
    "highlightthickness": 0,
}

button = tk.Button(window, text="Afficher la table de multiplication", command=on_button_click, **button_style)
button.pack(pady=10)

output_label = tk.Label(window, text="", bg=output_bg_color, justify="left", font=output_font_style)
output_label.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

window.mainloop()
