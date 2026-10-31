import math


class CalculadoraEngine:

    def __init__(self):
        self.reset()

    def reset(self):
        """Limpia todo el estado de la calculadora (Botón C)."""
        self.pantalla = "0"
        self.memoria = 0.0
        self.operador_pendiente = None
        self.nueva_entrada = True
        self.historial = ""

    def borrar_entrada(self):
        """Limpia la entrada actual sin borrar la memoria (Botón CE)."""
        self.pantalla = "0"
        self.nueva_entrada = True

    def borrar_ultimo_caracter(self):
        """Borra el último dígito ingresado (Botón ⌫)."""
        if self.nueva_entrada:
            return

        if len(self.pantalla) > 1:
            self.pantalla = self.pantalla[:-1]
        else:
            self.pantalla = "0"
            self.nueva_entrada = True

    def ingresar_numero(self, digito: str):
        """Agrega un dígito o punto decimal a la pantalla."""
        if self.nueva_entrada:
            if digito == ".":
                self.pantalla = "0."
            else:
                self.pantalla = digito
            self.nueva_entrada = False
        else:
            if digito == "." and "." in self.pantalla:
                return  # Evitar múltiples puntos decimales
            self.pantalla += digito

    def operacion_binaria(self, nuevo_operador: str):
        """Maneja operadores que requieren dos números (+, -, *, /)."""
        valor_actual = float(self.pantalla)

        if self.operador_pendiente and not self.nueva_entrada:
            self._calcular_resultado_pendiente(valor_actual)
        else:
            self.memoria = valor_actual

        self.operador_pendiente = nuevo_operador
        self.historial = f"{self._formatear(self.memoria)} {nuevo_operador}"
        self.nueva_entrada = True

    def calcular_igual(self):
        """Ejecuta la operación pendiente al presionar '='."""
        if self.operador_pendiente is None:
            return

        valor_actual = float(self.pantalla)
        self.historial = f"{self._formatear(self.memoria)} {self.operador_pendiente} {self._formatear(valor_actual)} ="
        self._calcular_resultado_pendiente(valor_actual)
        self.operador_pendiente = None
        self.nueva_entrada = True

    def _calcular_resultado_pendiente(self, valor_derecho: float):
        try:
            if self.operador_pendiente == "+":
                resultado = self.memoria + valor_derecho
            elif self.operador_pendiente == "-":
                resultado = self.memoria - valor_derecho
            elif self.operador_pendiente == "*":
                resultado = self.memoria * valor_derecho
            elif self.operador_pendiente == "/":
                if valor_derecho == 0:
                    self.pantalla = "Error"
                    self.operador_pendiente = None
                    self.nueva_entrada = True
                    return
                resultado = self.memoria / valor_derecho
            else:
                return

            self.memoria = resultado
            self.pantalla = self._formatear(resultado)
        except Exception:
            self.pantalla = "Error"
            self.nueva_entrada = True

    # --- Operaciones de Un Solo Botón ---

    def calcular_porcentaje(self):
        """Calcula el porcentaje (Botón %)."""
        valor = float(self.pantalla)
        if self.operador_pendiente in ("+", "-"):
            resultado = self.memoria * (valor / 100.0)
        else:
            resultado = valor / 100.0

        self.pantalla = self._formatear(resultado)
        self.nueva_entrada = True

    def calcular_raiz_cuadrada(self):
        """Calcula √x."""
        valor = float(self.pantalla)
        if valor < 0:
            self.pantalla = "Entrada no válida"
            self.nueva_entrada = True
            return
        resultado = math.sqrt(valor)
        self.pantalla = self._formatear(resultado)
        self.nueva_entrada = True

    def calcular_cuadrado(self):
        """Calcula x²."""
        valor = float(self.pantalla)
        resultado = valor**2
        self.pantalla = self._formatear(resultado)
        self.nueva_entrada = True

    def calcular_inverso(self):
        """Calcula 1/x."""
        valor = float(self.pantalla)
        if valor == 0:
            self.pantalla = "Error"
            self.nueva_entrada = True
            return
        resultado = 1.0 / valor
        self.pantalla = self._formatear(resultado)
        self.nueva_entrada = True

    def cambiar_signo(self):
        """Cambia el signo ±."""
        if self.pantalla == "0" or self.pantalla == "Error":
            return
        if self.pantalla.startswith("-"):
            self.pantalla = self.pantalla[1:]
        else:
            self.pantalla = "-" + self.pantalla

    def _formatear(self, valor: float) -> str:
        """Elimina decimales innecesarios (ej. 5.0 -> 5)."""
        if valor.is_integer():
            return str(int(valor))
        return str(round(valor, 8))