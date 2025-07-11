import tkinter as tk
from tkinter import messagebox
from updater import check_for_updates  # Importa tu módulo existente
import os
import sys

class Calculadora:
    def __init__(self, master):
        self.master = master
        self.configurar_ventana()
        self.crear_interfaz()
        self.programar_actualizacion()

    def configurar_ventana(self):
        self.master.title("Calculadora Pro v1.1.0")
        self.master.geometry("400x550")
        self.master.resizable(False, False)
        self.master.configure(bg="#f0f0f0")

    def crear_interfaz(self):
        # Estilo común para botones
        estilo_boton = {
            "font": ("Arial", 18),
            "bd": 3,
            "relief": tk.RIDGE,
            "width": 5
        }

        # Campo de resultado
        self.resultado = tk.StringVar()
        tk.Entry(
            self.master,
            textvariable=self.resultado,
            font=("Arial", 24),
            justify="right",
            bd=10,
            readonlybackground="#f0f0f0",
            state='readonly'
        ).grid(row=0, column=0, columnspan=4, pady=(20, 10), padx=10)

        # Botones numéricos y operadores
        botones = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        for (texto, fila, columna) in botones:
            tk.Button(
                self.master,
                text=texto,
                command=lambda t=texto: self.accion_boton(t),
                **estilo_boton
            ).grid(row=fila, column=columna, padx=2, pady=2)

        # Botones especiales
        tk.Button(
            self.master,
            text="C",
            command=self.limpiar,
            bg="#ff6b6b",
            fg="white",
            **{**estilo_boton, "width": 12}
        ).grid(row=5, column=0, columnspan=2, pady=10)

        tk.Button(
            self.master,
            text="↻ Actualizar",
            command=self.ejecutar_actualizacion,
            bg="#4CAF50",
            fg="white",
            **{**estilo_boton, "width": 12}
        ).grid(row=5, column=2, columnspan=2)

    def programar_actualizacion(self):
        """ Programa la verificación de actualizaciones después de 1.5 segundos """
        self.master.after(1500, self.ejecutar_actualizacion)

    def ejecutar_actualizacion(self):
        try:
            check_for_updates()  # Usa tu función existente en updater.py
        except Exception as e:
            messagebox.showerror("Error", f"Falló la actualización:\n{str(e)}")

    def accion_boton(self, texto):
        if texto == '=':
            try:
                self.resultado.set(str(eval(self.resultado.get())))
            except Exception:
                self.resultado.set("Error")
        else:
            self.resultado.set(self.resultado.get() + texto)

    def limpiar(self):
        self.resultado.set("")

def iniciar_aplicacion():
    try:
        # Configuración para alta resolución en Windows
        if os.name == 'nt':
            from ctypes import windll
            windll.shcore.SetProcessDpiAwareness(1)
    except:
        pass

    root = tk.Tk()
    Calculadora(root)
    root.mainloop()

if __name__ == "__main__":
    iniciar_aplicacion()
