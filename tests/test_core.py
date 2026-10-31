import pytest
from src.core import CalculadoraEngine


@pytest.fixture
def calc():
    return CalculadoraEngine()


def test_ingreso_numeros(calc):
    calc.ingresar_numero("5")
    calc.ingresar_numero("3")
    assert calc.pantalla == "53"


def test_punto_decimal(calc):
    calc.ingresar_numero("3")
    calc.ingresar_numero(".")
    calc.ingresar_numero("1")
    calc.ingresar_numero(".")  # Debe ignorarse el segundo punto
    assert calc.pantalla == "3.1"


def test_suma_basica(calc):
    calc.ingresar_numero("5")
    calc.operacion_binaria("+")
    calc.ingresar_numero("3")
    calc.calcular_igual()
    assert calc.pantalla == "8"


def test_operaciones_encadenadas(calc):
    calc.ingresar_numero("5")
    calc.operacion_binaria("+")
    calc.ingresar_numero("3")
    calc.operacion_binaria("*")  # Debe calcular 5+3=8 primero
    assert calc.pantalla == "8"
    calc.ingresar_numero("2")
    calc.calcular_igual()
    assert calc.pantalla == "16"


def test_division_por_cero(calc):
    calc.ingresar_numero("8")
    calc.operacion_binaria("/")
    calc.ingresar_numero("0")
    calc.calcular_igual()
    assert calc.pantalla == "Error"


def test_raiz_cuadrada_negativa(calc):
    calc.ingresar_numero("9")
    calc.cambiar_signo()
    calc.calcular_raiz_cuadrada()
    assert calc.pantalla == "Entrada no válida"


def test_borrar_caracter(calc):
    calc.ingresar_numero("1")
    calc.ingresar_numero("2")
    calc.ingresar_numero("3")
    calc.borrar_ultimo_caracter()
    assert calc.pantalla == "12"