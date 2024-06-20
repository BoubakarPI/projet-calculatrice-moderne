import tkinter as tk


def on_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(current_entry.get())
            current_entry.delete(0, tk.END)
            current_entry.insert(tk.END, str(result))
        except Exception as e:
            current_entry.delete(0, tk.END)
            current_entry.insert(tk.END, "Error")
    elif text == "C":
        current_entry.delete(0, tk.END)
    else:
        current_entry.insert(tk.END, text)


root = tk.Tk()
root.title("Calculatrice")

font_family = ('Arial', 20)

# Entry pour l'affichage des résultats

display_frame = tk.Frame(root)
display_frame.grid(row=0, column=0, columnspan=4, sticky="nsew")

expression_total = tk.Label(display_frame, bg="white", fg="black", font=("Arial", 24))
expression_total.pack(expand=True, fill="both")

current_entry = tk.Entry(display_frame, justify="right", bg="white", fg="black", font=("Arial", 40, "bold"))
current_entry.pack(expand=True, fill="both")

btn_frame = tk.Frame(root)
btn_frame.grid(row=1, column=0, columnspan=4, sticky="nsew")

specials_btn_frame = tk.Frame(btn_frame)
specials_btn_frame.pack(expand=True, fill="both")

normal_btn_frame = tk.Frame(btn_frame)
normal_btn_frame.pack(expand=True, fill="both")

# Liste des boutons avec leur texte et position
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('*', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('+', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('=', 4, 3)
]
bouttons_specials = [
    ('exp', 1, 0), ('x²', 1, 1), ('√', 1, 3), ('÷', 1, 4)
]

# Création des boutons
for (text, row, column) in buttons:
    btn = tk.Button(normal_btn_frame, text=text, padx=20, pady=20, bg="white", fg="black", font=("Arial", 20), )
    btn.grid(row=row, column=column, sticky="nsew")
    btn.bind("<Button-1>", on_click)

# Création des boutons spéciaux
for (text, row, column) in bouttons_specials:
    btn = tk.Button(specials_btn_frame, text=text, padx=20, pady=20, bg="white", fg="black", font=("Arial", 20), )
    btn.grid(row=row, column=column, sticky="nsew")
    btn.bind("<Button-1>", on_click)

# Configuration des lignes et colonnes pour qu'elles s'adaptent à la fenêtre
for i in range(6):  # 6 lignes au total
    root.grid_rowconfigure(i, weight=1)
for i in range(4):  # 4 colonnes au total
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
