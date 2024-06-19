import math
import tkinter as tk


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculatrice")

        self.total_expression = ""
        self.current_expression = ""

        self.display_frame = self.create_display_frame()

        self.total_label, self.label = self.create_display_labels()

        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), '.': (4, 1)
        }

        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}

        self.buttons_frame = self.create_buttons_frame()

        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()
        self.bind_keys()

    def bind_keys(self):
        self.root.bind("<Return>", lambda event: self.evaluate())
        for key in self.digits:
            self.root.bind(str(key), lambda event, digit=key: self.add_to_expression(digit))
        for key in self.operations:
            self.root.bind(key, lambda event, operator=key: self.append_operator(operator))

    def create_special_buttons(self):
        self.create_clear_button()
        self.create_equals_button()
        self.create_exponent_button()
        self.create_square_button()
        self.create_sqrt_button()

    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg="white", fg="black",
                               padx=24, font=("Arial", 24))
        total_label.pack(expand=True, fill="both")

        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg="white", fg="black", padx=24,
                         font=("Arial", 40, "bold"))
        label.pack(expand=True, fill="both")

        return total_label, label

    def create_display_frame(self):
        frame = tk.Frame(self.root, height=221, bg="white")
        frame.pack(expand=True, fill="both")
        return frame

    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.update_label()

    def append_operator(self, operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_total_label()
        self.update_label()

    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), bg="white", fg="black", font=("Arial", 24, "bold"),
                               borderwidth=0, command=lambda x=digit: self.add_to_expression(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg="white", fg="black", font=("Arial", 20),
                               borderwidth=0, command=lambda x=operator: self.append_operator(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1

    def clear(self):
        self.current_expression = ""
        self.total_expression = ""
        self.update_label()
        self.update_total_label()

    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text="C", bg="white", fg="black", font=("Arial", 20), borderwidth=0,
                           command=self.clear)
        button.grid(row=4, column=3, sticky=tk.NSEW)

    def evaluate(self):
        self.total_expression += self.current_expression
        self.update_total_label()
        try:
            self.current_expression = str(eval(self.total_expression))
            self.total_expression = ""
        except Exception as e:
            self.current_expression = "Error"
        finally:
            self.update_label()

    def create_equals_button(self):
        button = tk.Button(self.buttons_frame, text="=", bg="white", fg="black", font=("Arial", 20), borderwidth=0,
                           command=self.evaluate)
        button.grid(row=4, column=4, columnspan=1, sticky=tk.NSEW)

    def create_buttons_frame(self):
        frame = tk.Frame(self.root)
        frame.pack(expand=True, fill="both")
        for x in range(1, 5):
            frame.rowconfigure(x, weight=1)
            frame.columnconfigure(x, weight=1)
        return frame

    def update_total_label(self):
        self.total_label.config(text=self.total_expression)

    def update_label(self):
        self.label.config(text=self.current_expression[:11])

    def square(self):
        self.current_expression = str(eval(f"{self.current_expression}**2"))
        self.update_label()

    def sqrt(self):
        self.current_expression = str(math.sqrt(float(self.current_expression)))
        self.update_label()

    def exponent(self):
        self.current_expression += "**"
        self.update_label()

    def create_square_button(self):
        button = tk.Button(self.buttons_frame, text="x²", bg="white", fg="black", font=("Arial", 20), borderwidth=0,
                           command=self.square)
        button.grid(row=0, column=2, sticky=tk.NSEW)

    def create_sqrt_button(self):
        button = tk.Button(self.buttons_frame, text="√", bg="white", fg="black", font=("Arial", 20), borderwidth=0,
                           command=self.sqrt)
        button.grid(row=0, column=3, sticky=tk.NSEW)

    def create_exponent_button(self):
        button = tk.Button(self.buttons_frame, text="exp", bg="white", fg="black", font=("Arial", 20), borderwidth=0,
                           command=self.exponent)
        button.grid(row=0, column=1, sticky=tk.NSEW)


if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
