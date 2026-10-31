import sys
import os
import tkinter as tk
from tkinter import font

# Asegurar importación de core sin importar desde dónde se ejecute el script
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.core import CalculadoraEngine

# Interfaz clásica - modificar a criterio propio 
class CalculadoraGUI:

    def __init__(self, root: tk.Tk):
        self.root = root
        self.engine = CalculadoraEngine()

        # Configuración de la ventana principal
        self.root.title("Calculadora")
        self.root.geometry("340x480")
        self.root.minsize(300, 420)
        self.root.configure(bg="#F3F3F3")

        self._configurar_fuentes()
        self._crear_pantalla()
        self._crear_botones()
        self._vincular_teclado()

    def _configurar_fuentes(self):
        self.fuente_historial = font.Font(family="Segoe UI", size=10)
        self.fuente_pantalla = font.Font(family="Segoe UI", size=26, weight="bold")
        self.fuente_botones = font.Font(family="Segoe UI", size=12)
        self.fuente_operadores = font.Font(family="Segoe UI", size=12, weight="bold")

    def _crear_pantalla(self):
        frame_pantalla = tk.Frame(self.root, bg="#F3F3F3", padx=10, pady=5)
        frame_pantalla.pack(expand=False, fill="both")

        # Pantalla de historial (expresión previa)
        self.label_historial = tk.Label(
            frame_pantalla,
            text="",
            anchor="e",
            bg="#F3F3F3",
            fg="#666666",
            font=self.fuente_historial,
        )
        self.label_historial.pack(fill="x")

        # Pantalla principal (número actual)
        self.label_pantalla = tk.Label(
            frame_pantalla,
            text="0",
            anchor="e",
            bg="#F3F3F3",
            fg="#000000",
            font=self.fuente_pantalla,
        )
        self.label_pantalla.pack(fill="x")

    def _crear_botones(self):
        frame_botones = tk.Frame(self.root, bg="#F3F3F3", padx=5, pady=5)
        frame_botones.pack(expand=True, fill="both")

        # Configuración de grilla responsiva (6 filas x 4 columnas)
        for i in range(6):
            frame_botones.rowconfigure(i, weight=1)
        for j in range(4):
            frame_botones.columnconfigure(j, weight=1)

        # Matriz de botones: orden (Texto, Fila, Columna, Tipo)
        botones = [
            ("%", 0, 0, "op_ind"),
            ("CE", 0, 1, "op_ind"),
            ("C", 0, 2, "op_ind"),
            ("⌫", 0, 3, "op_ind"),
            ("1/x", 1, 0, "op_ind"),
            ("x²", 1, 1, "op_ind"),
            ("√x", 1, 2, "op_ind"),
            ("÷", 1, 3, "op_bin"),
            ("7", 2, 0, "num"),
            ("8", 2, 1, "num"),
            ("9", 2, 2, "num"),
            ("×", 2, 3, "op_bin"),
            ("4", 3, 0, "num"),
            ("5", 3, 1, "num"),
            ("6", 3, 2, "num"),
            ("-", 3, 3, "op_bin"),
            ("1", 4, 0, "num"),
            ("2", 4, 1, "num"),
            ("3", 4, 2, "num"),
            ("+", 4, 3, "op_bin"),
            ("±", 5, 0, "num"),
            ("0", 5, 1, "num"),
            (".", 5, 2, "num"),
            ("=", 5, 3, "igual"),
        ]

        for texto, fila, col, tipo in botones:
            self._crear_boton(frame_botones, texto, fila, col, tipo)

    def _crear_boton(self, parent, texto: str, fila: int, col: int, tipo: str):
        # Estilos según el tipo de botón elegido arbitrariamente Por lo general colores convencionales 
        if tipo == "num":
            bg, fg, font_use = "#FFFFFF", "#000000", self.fuente_botones
        elif tipo == "igual":
            bg, fg, font_use = "#005A9E", "#FFFFFF", self.fuente_operadores
        else:
            bg, fg, font_use = "#F9F9F9", "#000000", self.fuente_operadores

        btn = tk.Button(
            parent,
            text=texto,
            bg=bg,
            fg=fg,
            font=font_use,
            bd=1,
            relief="groove",
            activebackground="#E5E5E5",
            command=lambda: self._procesar_accion(texto),
        )
        btn.grid(row=fila, column=col, sticky="nsew", padx=2, pady=2)

    def _vincular_teclado(self):
        """Mapea las teclas físicas a las acciones de la calculadora."""
        self.root.bind("<Key>", self._manejar_evento_teclado)

    def _manejar_evento_teclado(self, event):
        char = event.char
        key = event.keysym

        if char in "0123456789.":
            self._procesar_accion(char)
        elif char == "+":
            self._procesar_accion("+")
        elif char == "-":
            self._procesar_accion("-")
        elif char == "*":
            self._procesar_accion("×")
        elif char == "/":
            self._procesar_accion("÷")
        elif key in ("Return", "KP_Enter"):
            self._procesar_accion("=")
        elif key == "BackSpace":
            self._procesar_accion("⌫")
        elif key == "Escape":
            self._procesar_accion("C")

    def _procesar_accion(self, texto_boton: str):
        """Enruta la acción del usuario hacia el motor matemático."""
        if texto_boton in "0123456789.":
            self.engine.ingresar_numero(texto_boton)
        elif texto_boton in ("+", "-", "×", "÷"):
            # Traducir símbolos visuales a operadores estándar
            op_map = {"×": "*", "÷": "/"}
            self.engine.operacion_binaria(op_map.get(texto_boton, texto_boton))
        elif texto_boton == "=":
            self.engine.calcular_igual()
        elif texto_boton == "C":
            self.engine.reset()
        elif texto_boton == "CE":
            self.engine.borrar_entrada()
        elif texto_boton == "⌫":
            self.engine.borrar_ultimo_caracter()
        elif texto_boton == "%":
            self.engine.calcular_porcentaje()
        elif texto_boton == "√x":
            self.engine.calcular_raiz_cuadrada()
        elif texto_boton == "x²":
            self.engine.calcular_cuadrado()
        elif texto_boton == "1/x":
            self.engine.calcular_inverso()
        elif texto_boton == "±":
            self.engine.cambiar_signo()

        self._actualizar_interfaz()

    def _actualizar_interfaz(self):
        """Refleja los cambios del motor en los Labels de pantalla."""
        self.label_pantalla.config(text=self.engine.pantalla)
        self.label_historial.config(text=self.engine.historial)


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraGUI(root)
    root.mainloop()