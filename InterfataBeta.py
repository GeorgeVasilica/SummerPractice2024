import tkinter as tk
from tkinter import ttk

class Interfata():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('350x300')
        self.root.title('Interfata simpla')
        self.mainframe = tk.Frame(self.root, background='grey')
        self.mainframe.pack(fill='both', expand=True)

        self.vcmd = (self.root.register(self.validat), '%P')

        # Label și Spinbox pentru Voltaj
        self.label1 = ttk.Label(self.mainframe, text='Voltaj', background='grey', font=('Brass Mono', 10))
        self.label1.grid(row=0, column=0, padx=10, pady=10)
        self.voltaj = ttk.Spinbox(self.mainframe, from_=9, to=13.5, increment=0.01, validate='key', validatecommand=self.vcmd)
        self.voltaj.grid(row=1, column=0, padx=10, pady=10)

        # Label și Spinbox pentru Amper
        self.label2 = ttk.Label(self.mainframe, text='Amper', background='grey', font=('Brass Mono', 10))
        self.label2.grid(row=2, column=0, padx=10, pady=10)
        self.amper = ttk.Spinbox(self.mainframe, from_=9, to=13.5, increment=0.01, validate='key', validatecommand=self.vcmd)
        self.amper.grid(row=3, column=0, padx=10, pady=10)

        # Label și Spinbox pentru Puterea
        self.label3 = ttk.Label(self.mainframe, text='Puterea', background='grey', font=('Brass Mono', 10))
        self.label3.grid(row=4, column=0, padx=10, pady=10)
        self.puterea = ttk.Spinbox(self.mainframe, from_=9, to=13.5, increment=0.01, validate='key', validatecommand=self.vcmd)
        self.puterea.grid(row=5, column=0, padx=10, pady=10)

        self.root.mainloop()

    # Funcția de validare
    def validat(self, P):
        if P == "":
            return True  # Permite ștergerea valorii
        try:
            float(P)
            return True  # Permite introducerea dacă valoarea poate fi convertit în float
        except ValueError:
            return False  # Blochează introducerea dacă valoarea nu poate fi convertit în float

if __name__ == '__main__':
    Interfata()
