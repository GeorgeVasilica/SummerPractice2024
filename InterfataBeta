import tkinter as tk
from tkinter import ttk
import keyboard


def validare_tasta(key):
    if key.isdigit():
        print(key)
        return key


class Interfata():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('350x250')
        self.root.title('Interfata simpla')
        self.mainframe = tk.Frame(self.root, background='grey')
        self.mainframe.pack(fill='both', expand=True)

        self.label1 = ttk.Label(self.mainframe, text='Voltaj', background='grey', font=('Brass Mono', 10))
        self.label1.grid(row=0, column=0, padx=10, pady=10)
       # self.text1 = ttk.Spinbox(self.mainframe, background='white', increment=0.01, from_=9, to=13.5)
       # self.text1.grid(row=1, column=0, padx=10, pady=10)
        self.text1 = ttk.Entry(self.mainframe,)
        self.text1.grid(row=1, column=0, padx=10, pady=10)

        self.label2 = ttk.Label(self.mainframe, text='Amper', background='grey', font=('Brass Mono', 10))
        self.label2.grid(row=2, column=0, padx=10, pady=10)
        self.text2 = ttk.Spinbox(self.mainframe, background='white', increment=0.01, from_=9, to=13.5)
        self.text2.grid(row=3, column=0, padx=10, pady=10)

        self.root.mainloop()
        return


if __name__ == '__main__':
    Interfata()

