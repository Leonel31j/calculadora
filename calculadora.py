import tkinter as tk

class Calculadora:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora")

        self.resultado = tk.StringVar()

        self.entrada = tk.Entry(master, textvariable=self.resultado, font=("Arial", 16), bd=10, insertwidth=2, width=14, borderwidth=4)
        self.entrada.grid(row=0, column=0, columnspan=4)

        botones = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        fila = 1
        col = 0
        for boton in botones:
            tk.Button(master, text=boton, padx=20, pady=20, font=("Arial", 16), command=lambda b=boton: self.click(b)).grid(row=fila, column=col)
            col += 1
            if col > 3:
                col = 0
                fila += 1

        tk.Button(master, text='C', padx=20, pady=20, font=("Arial", 16), command=self.clear).grid(row=fila, column=0)

    def click(self, boton):
        if boton == '=':
            try:
                self.resultado.set(eval(self.resultado.get()))
            except Exception as e:
                self.resultado.set("Error")
        else:
            self.resultado.set(self.resultado.get() + boton)

    def clear(self):
        self.resultado.set("")

if __name__ == "__main__":
    root = tk.Tk()
    calculadora = Calculadora(root)
    root.mainloop()
