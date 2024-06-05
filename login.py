import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from datetime import datetime

def ouvrir_fenetre_utilisateur():
    fenetre_utilisateur = tk.Toplevel(fenetre)
    fenetre_utilisateur.title("Login Utilisateur")
    fenetre_utilisateur.geometry("420x480")
    
    # Style
    style = ttk.Style()
    style.configure('TLabel', background='#f0f0f0')
    style.configure('TButton', background='#2196f3', foreground='#2196f3')

    # Header
    header = ttk.Label(fenetre_utilisateur, text="Login", font=('Arial', 16, 'bold'))
    header.grid(row=0, columnspan=2, padx=10, pady=10)

    def valider_saisie_utilisateur():
        email = champ_email.get()
        username = champ_username.get()
        password = champ_password.get()
        confirmer = champ_confirmer.get()

        if not email or not username or not password or not confirmer:
            messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")
        elif password != confirmer:
            messagebox.showerror("Erreur", "Les mots de passe ne correspondent pas.")
        else:
            ouvrir_fenetre_commande()

    # Layout
    champ_email_label = ttk.Label(fenetre_utilisateur, text="Email")
    champ_email_label.grid(row=1, column=0, padx=10, pady=5)
    champ_email = ttk.Entry(fenetre_utilisateur)
    champ_email.grid(row=1, column=1, padx=10, pady=5)

    champ_username_label = ttk.Label(fenetre_utilisateur, text="Nom d'utilisateur")
    champ_username_label.grid(row=2, column=0, padx=10, pady=5)
    champ_username = ttk.Entry(fenetre_utilisateur)
    champ_username.grid(row=2, column=1, padx=10, pady=5)

    champ_password_label = ttk.Label(fenetre_utilisateur, text="Mot de passe")
    champ_password_label.grid(row=3, column=0, padx=10, pady=5)
    champ_password = ttk.Entry(fenetre_utilisateur, show="*")
    champ_password.grid(row=3, column=1, padx=10, pady=5)

    champ_confirmer_label = ttk.Label(fenetre_utilisateur, text="Confirmer le mot de passe")
    champ_confirmer_label.grid(row=4, column=0, padx=10, pady=5)
    champ_confirmer = ttk.Entry(fenetre_utilisateur, show="*")
    champ_confirmer.grid(row=4, column=1, padx=10, pady=5)

    bouton_valider = ttk.Button(fenetre_utilisateur, text="Valider", command=valider_saisie_utilisateur)
    bouton_valider.grid(row=5, columnspan=2, padx=10, pady=10)

def upload_file():
    filename = filedialog.askopenfilename()
    nom_fichier_entry.delete(0, tk.END)
    nom_fichier_entry.insert(0, filename)

def ouvrir_fenetre_commande():
    fenetre_commande = tk.Toplevel(fenetre)
    fenetre_commande.title("Commande")
    fenetre_commande.geometry("520x480")
    
    # Style
    style = ttk.Style()
    style.configure('TLabel', background='#f0f0f0')
    style.configure('TButton', background='#2196f3', foreground='#2196f3')

    # Get current date and time
    now = datetime.now()
    date_heure = now.strftime("%d/%m/%Y %H:%M:%S")

    # Header
    header = ttk.Label(fenetre_commande, text="Commande", font=('Arial', 16, 'bold'))
    header.grid(row=0, columnspan=3, padx=10, pady=10)

    # Layout for additional fields
    cin_label = ttk.Label(fenetre_commande, text="CIN")
    cin_label.grid(row=1, column=0, padx=10, pady=5)
    cin_entry = ttk.Entry(fenetre_commande)
    cin_entry.grid(row=1, column=1, padx=10, pady=5)

    nom_label = ttk.Label(fenetre_commande, text="Nom")
    nom_label.grid(row=2, column=0, padx=10, pady=5)
    nom_entry = ttk.Entry(fenetre_commande)
    nom_entry.grid(row=2, column=1, padx=10, pady=5)

    fichier_label = ttk.Label(fenetre_commande, text="Insérer un fichier")
    fichier_label.grid(row=3, column=0, padx=10, pady=5)

    nom_fichier_entry = ttk.Entry(fenetre_commande)
    nom_fichier_entry.grid(row=3, column=1, padx=10, pady=5)

    upload_button = ttk.Button(fenetre_commande, text="Upload", command=upload_file)
    upload_button.grid(row=3, column=2, padx=10, pady=5)

    date_heure_label = ttk.Label(fenetre_commande, text="Date et Heure")
    date_heure_label.grid(row=4, column=0, padx=10, pady=5)
    date_heure_entry = ttk.Label(fenetre_commande, text=date_heure)
    date_heure_entry.grid(row=4, column=1, padx=10, pady=5)

    bouton_commander = ttk.Button(fenetre_commande, text="Commander")
    bouton_commander.grid(row=5, columnspan=3, padx=10, pady=10)

def ouvrir_fenetre_administrateur():
    fenetre_administrateur = tk.Toplevel(fenetre)
    fenetre_administrateur.title("Login Administrateur")
    fenetre_administrateur.geometry("360x480")
    
    # Style
    style = ttk.Style()
    style.configure('TLabel', background='#f0f0f0')
    style.configure('TButton', background='#2196f3', foreground='#2196f3')

    # Header
    header = ttk.Label(fenetre_administrateur, text="Login Administrateur", font=('Arial', 16, 'bold'))
    header.grid(row=0, columnspan=2, padx=10, pady=10)

    def valider_saisie_administrateur():
        username = champ_username.get()
        password = champ_password.get()

        if not username or not password:
            messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")
        else:
            messagebox.showinfo("Succès", "Saisie administrateur valide.")

    # Layout
    champ_username_label = ttk.Label(fenetre_administrateur, text="Nom d'utilisateur")
    champ_username_label.grid(row=1, column=0, padx=10, pady=5)
    champ_username = ttk.Entry(fenetre_administrateur)
    champ_username.grid(row=1, column=1, padx=10, pady=5)

    champ_password_label = ttk.Label(fenetre_administrateur, text="Mot de passe")
    champ_password_label.grid(row=2, column=0, padx=10, pady=5)
    champ_password = ttk.Entry(fenetre_administrateur, show="*")
    champ_password.grid(row=2, column=1, padx=10, pady=5)

    bouton_connexion = ttk.Button(fenetre_administrateur, text="Connexion", command=valider_saisie_administrateur)
    bouton_connexion.grid(row=3, columnspan=2, padx=10, pady=10)

# Main window
fenetre = tk.Tk()
fenetre.title("Poka Yoke")
fenetre.geometry("480x480")

# Style
style = ttk.Style()
style.configure('TLabel', background='#f0f0f0')
style.configure('TButton', background='#2196f3', foreground='#2196f3')

# Layout
titre = ttk.Label(fenetre, text="Méthode de prévention des erreurs", font=('Arial', 16, 'bold'))
titre.grid(row=0, columnspan=2, padx=10, pady=10)

bouton_utilisateur = ttk.Button(fenetre, text="Utilisateur", command=ouvrir_fenetre_utilisateur)
bouton_utilisateur.grid(row=1, column=0, padx=10, pady=10)

bouton_administrateur = ttk.Button(fenetre, text="Administrateur", command=ouvrir_fenetre_administrateur)
bouton_administrateur.grid(row=1, column=1, padx=10, pady=10)

fenetre.mainloop()
