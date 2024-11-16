import tkinter as tk
from tkinter import ttk

# Création de la fenêtre principale
root = tk.Tk()
root.title("Gestionnaire de Mots de Passe")
root.geometry("600x400")
root.config(bg="#1c1c1c")

# Onglets
notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True, padx=10, pady=10)

# Styles ttk pour un design sombre
style = ttk.Style()
style.theme_use("clam")
style.configure("TNotebook", background="#1c1c1c", tabmargins=[2, 5, 2, 0])
style.configure("TNotebook.Tab", background="#333333", foreground="white", padding=[10, 5])
style.map("TNotebook.Tab", background=[("selected", "#555555")])

# Onglet "Ajouter mot de passe"
frame_add = tk.Frame(notebook, bg="#2b2b2b")
notebook.add(frame_add, text="Ajouter mot de passe")

tk.Label(frame_add, text="Nom du site :", bg="#2b2b2b", fg="white").pack(pady=5)
tk.Entry(frame_add).pack(fill="x", padx=20, pady=5)

tk.Label(frame_add, text="Email :", bg="#2b2b2b", fg="white").pack(pady=5)
tk.Entry(frame_add).pack(fill="x", padx=20, pady=5)

tk.Label(frame_add, text="Mot de passe :", bg="#2b2b2b", fg="white").pack(pady=5)
tk.Entry(frame_add, show="*").pack(fill="x", padx=20, pady=5)

tk.Button(frame_add, text="Enregistrer", bg="#444", fg="white").pack(pady=10)

# Onglet "Voir mots de passe"
frame_view = tk.Frame(notebook, bg="#2b2b2b")
notebook.add(frame_view, text="Voir mots de passe")

tk.Label(frame_view, text="(Liste des mots de passe)", bg="#2b2b2b", fg="white").pack(pady=20)

# Onglet "Générer mot de passe"
frame_generate = tk.Frame(notebook, bg="#2b2b2b")
notebook.add(frame_generate, text="Générer mot de passe")

tk.Label(frame_generate, text="Longueur :", bg="#2b2b2b", fg="white").pack(pady=5)
tk.Spinbox(frame_generate, from_=8, to=32, bg="#444", fg="white").pack(pady=5)
tk.Button(frame_generate, text="Générer", bg="#444", fg="white").pack(pady=10)

root.mainloop()
