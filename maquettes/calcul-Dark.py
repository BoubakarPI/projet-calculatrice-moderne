import tkinter as tk


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculatrice")

        self.total_expression = ""
        self.current_expression = ""

        self.display_frame = tk.Frame(self.root, height=221, bg="#17171C")
        self.display_frame.pack(expand=True, fill="both")

        self.total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg="#17171C",
                                    fg="#4E505F",
                                    padx=24, font=("Arial", 24))
        self.total_label.pack(expand=True, fill="both")

        self.current_label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg="#17171C",
                                      fg="white",
                                      padx=24, font=("Arial", 40, "bold"))
        self.current_label.pack(expand=True, fill="both")

        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), '.': (4, 1)
        }

        self.operations = {
            "/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"
        }

        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack(expand=True, fill="both")

        for x in range(1, 5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)

        self.create_digit_and_operator_buttons()
        self.create_special_buttons()
        self.bind_keys()

    def bind_keys(self):
        self.root.bind("<Return>", lambda event: self.evaluate())
        for key in self.digits:
            self.root.bind(str(key), lambda event, digit=key: self.add_to_expression(digit))
        for key in self.operations:
            self.root.bind(key, lambda event, operator=key: self.append_operator(operator))

    def create_digit_and_operator_buttons(self):
        for digit, grid_value in self.digits.items():
            tk.Button(self.buttons_frame, text=str(digit), bg="#2E2F38", fg="white", font=("Arial", 24, "bold"),
                      borderwidth=1, command=lambda x=digit: self.add_to_expression(x)).grid(row=grid_value[0],
                                                                                             column=grid_value[1],
                                                                                             sticky=tk.NSEW)

        i = 0
        primaryColorLight = "#4B5EFC"
        for operator, symbol in self.operations.items():
            tk.Button(self.buttons_frame, text=symbol, bg=primaryColorLight, fg="white", font=("Arial", 20),
                      borderwidth=0,
                      command=lambda x=operator: self.append_operator(x)).grid(row=i, column=4, sticky=tk.NSEW)
            i += 1

    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.update_label()

    def append_operator(self, operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_total_label()
        self.update_label()

    def clear(self):
        self.current_expression = ""
        self.total_expression = ""
        self.update_label()
        self.update_total_label()

    def evaluate(self):
        self.total_expression += self.current_expression
        self.update_total_label()
        try:
            self.current_expression = str(eval(self.total_expression))
            self.total_expression = ""
        except Exception as e:
            self.current_expression = "Erreur"
        finally:
            self.update_label()

    def create_special_buttons(self):
        primaryColorLight = "#4B5EFC"
        tk.Button(self.buttons_frame, text="C", bg="#2E2F38", fg="white", font=("Arial", 20), borderwidth=0,
                  command=self.clear).grid(row=4, column=3, sticky=tk.NSEW)
        tk.Button(self.buttons_frame, text="=", bg=primaryColorLight, fg="white", font=("Arial", 20), borderwidth=0,
                  command=self.evaluate).grid(row=4, column=4, sticky=tk.NSEW)
        tk.Button(self.buttons_frame, text="x²", bg="#4E505F", fg="white", font=("Arial", 20), borderwidth=0,
                  command=lambda: self.add_to_expression("**2")).grid(row=0, column=2, sticky=tk.NSEW)
        tk.Button(self.buttons_frame, text="√", bg="#4E505F", fg="white", font=("Arial", 20), borderwidth=0,
                  command=lambda: self.add_to_expression("math.sqrt(")).grid(row=0, column=3, sticky=tk.NSEW)
        tk.Button(self.buttons_frame, text="exp", bg="#4E505F", fg="white", font=("Arial", 20), borderwidth=0,
                  command=lambda: self.add_to_expression("**")).grid(row=0, column=1, sticky=tk.NSEW)

    def update_total_label(self):
        self.total_label.config(text=self.total_expression)

    def update_label(self):
        self.current_label.config(text=self.current_expression[:11])


if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
