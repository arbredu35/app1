import tkinter as tk

def copy_text(event):
    widget = event.widget
    if isinstance(widget, tk.Entry):
        root.clipboard_clear()
        root.clipboard_append(widget.get())
        root.update()

root = tk.Tk()
root.geometry("500x300")
root.config(bg="#1e1e1e")
root.title("Gestionnaire de Mots de Passe")

# Champs d'entrée
entries = []
for i, label_text in enumerate(["Nom du site", "Email/Username", "Mot de passe"]):
    tk.Label(root, text=label_text, bg="#1e1e1e", fg="white").pack(anchor="w", padx=20, pady=5)
    entry = tk.Entry(root, bg="#2b2b2b", fg="white", insertbackground="white", relief="flat")
    entry.pack(fill="x", padx=20, pady=5)
    entries.append(entry)

# Menu contextuel
menu = tk.Menu(root, tearoff=0)
menu.add_command(label="Copier", command=lambda: copy_text)
menu.add_command(label="Effacer", command=lambda: [e.delete(0, tk.END) for e in entries])

def show_menu(event):
    menu.post(event.x_root, event.y_root)

root.bind("<Button-3>", show_menu)
root.mainloop()
