import tkinter as tk

def toggle_password():
    if password_entry.cget('show') == '*':
        password_entry.config(show='')
    else:
        password_entry.config(show='*')

root = tk.Tk()
root.geometry("400x250")
root.config(bg="#202020")

# Champs
tk.Label(root, text="Mot de passe :", bg="#202020", fg="white").pack(pady=5)
password_entry = tk.Entry(root, bg="#2b2b2b", fg="white", show='*', relief="flat")
password_entry.pack(fill="x", padx=20, pady=5)

# Bouton toggle
toggle_button = tk.Button(root, text="Afficher/Masquer", command=toggle_password, bg="#333", fg="white")
toggle_button.pack(pady=10)

root.mainloop()
