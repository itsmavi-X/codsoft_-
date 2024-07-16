import tkinter as tk
from math import sin, cos, tan, sqrt, pow, radians

class AdvancedCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Advanced Calculator")
        self.geometry("400x600")

        self.expression = ""

        self.display_frame = self.create_display_frame()
        self.total_label, self.label = self.create_display_labels()

        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), '.': (4, 1)
        }

        self.operations = {
            '/': "\u00F7", '*': "\u00D7", '-': '-', '+': '+'
        }

        self.buttons_frame = self.create_buttons_frame()

        self.buttons_frame.rowconfigure(0, weight=1)
        for x in range(1, 5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)

        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()
        self.create_clear_button()
        self.create_equals_button()

    def create_display_frame(self):
        frame = tk.Frame(self, height=221, bg='grey')
        frame.pack(expand=True, fill='both')
        return frame

    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text=self.expression, anchor=tk.E, bg='grey', fg='white', padx=24, font=('Arial', 20))
        total_label.pack(expand=True, fill='both')

        label = tk.Label(self.display_frame, text='', anchor=tk.E, bg='grey', fg='white', padx=24, font=('Arial', 40, 'bold'))
        label.pack(expand=True, fill='both')

        return total_label, label

    def create_buttons_frame(self):
        frame = tk.Frame(self)
        frame.pack(expand=True, fill='both')
        return frame

    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), bg='white', fg='black', font=('Arial', 24, 'bold'), borderwidth=0, command=lambda x=digit: self.add_to_expression(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg='orange', fg='black', font=('Arial', 24, 'bold'), borderwidth=0, command=lambda x=operator: self.append_operator(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1

    def create_special_buttons(self):
        special_buttons = {
            'sin': (0, 1), 'cos': (0, 2), 'tan': (0, 3),
            '√': (4, 3), '^': (4, 4)
        }
        for text, grid_value in special_buttons.items():
            button = tk.Button(self.buttons_frame, text=text, bg='lightblue', fg='black', font=('Arial', 24, 'bold'), borderwidth=0, command=lambda x=text: self.add_special_function(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text='C', bg='red', fg='black', font=('Arial', 24, 'bold'), borderwidth=0, command=self.clear)
        button.grid(row=0, column=0, sticky=tk.NSEW)

    def create_equals_button(self):
        button = tk.Button(self.buttons_frame, text='=', bg='lightgreen', fg='black', font=('Arial', 24, 'bold'), borderwidth=0, command=self.evaluate)
        button.grid(row=4, column=0, columnspan=2, sticky=tk.NSEW)

    def add_to_expression(self, value):
        self.expression += str(value)
        self.update_label()

    def append_operator(self, operator):
        self.expression += operator
        self.update_label()

    def add_special_function(self, func):
        if func == '√':
            self.expression += 'sqrt('
        elif func == '^':
            self.expression += '**'
        else:
            self.expression += f'{func}('
        self.update_label()

    def clear(self):
        self.expression = ""
        self.update_label()
        self.total_label.config(text="")

    def update_label(self):
        self.label.config(text=self.expression[:11])

    def evaluate(self):
        try:
            self.expression = self.expression.replace('√', 'sqrt')
            self.expression = self.expression.replace('sin', 'sin(radians')
            self.expression = self.expression.replace('cos', 'cos(radians')
            self.expression = self.expression.replace('tan', 'tan(radians')
            self.expression = self.expression.replace("\u00F7", "/")
            self.expression = self.expression.replace("\u00D7", "*")
            self.total_label.config(text=self.expression)
            self.expression = str(eval(self.expression))
            self.update_label()
        except Exception as e:
            self.expression = "Error"
            self.update_label()

if __name__ == "__main__":
    calculator = AdvancedCalculator()
    calculator.mainloop()