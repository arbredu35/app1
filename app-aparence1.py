import tkinter as tk

root = tk.Tk()
root.title("Gestionnaire de Mots de Passe")
root.geometry("600x400")
root.config(bg="#121212")

# Menu latéral
sidebar = tk.Frame(root, bg="#333333", width=150)
sidebar.pack(side="left", fill="y")

title = tk.Label(sidebar, text="Options", bg="#333333", fg="white", font=("Arial", 14, "bold"))
title.pack(pady=20)

btn1 = tk.Button(sidebar, text="Voir", bg="#444", fg="white", relief="flat", font=("Arial", 12), cursor="hand2")
btn1.pack(fill="x", pady=20, padx=20)

btn2 = tk.Button(sidebar, text="Générer", bg="#444", fg="white", relief="flat", font=("Arial", 12), cursor="hand2")
btn2.pack(fill="x", pady=20, padx=20)

btn3 = tk.Button(sidebar, text="Ajouter", bg="#444", fg="white", relief="flat", font=("Arial", 12), cursor="hand2")
btn3.pack(fill="x", pady=20, padx=20)

# Section centrale
center = tk.Frame(root, bg="#121212")
center.pack(side="right", fill="both", expand=True)

site_label = tk.Label(center, text="Nom du site :", bg="#121212", fg="white", font=("Arial", 12))
site_label.pack(anchor="w", padx=20, pady=5)
site_entry = tk.Entry(center, bg="#2b2b2b", fg="white", font=("Arial", 12), relief="flat")
site_entry.pack(fill="x", padx=20)

username_label = tk.Label(center, text="Email/Username :", bg="#121212", fg="white", font=("Arial", 12))
username_label.pack(anchor="w", padx=20, pady=5)
username_entry = tk.Entry(center, bg="#2b2b2b", fg="white", font=("Arial", 12), relief="flat")
username_entry.pack(fill="x", padx=20)

password_label = tk.Label(center, text="Mot de passe :", bg="#121212", fg="white", font=("Arial", 12))
password_label.pack(anchor="w", padx=20, pady=5)
password_entry = tk.Entry(center, bg="#2b2b2b", fg="white", font=("Arial", 12), relief="flat")
password_entry.pack(fill="x", padx=20)

root.mainloop()
