#  Arquitectura de Software: Clean Architecture

El proyecto aplica una separación estricta de responsabilidades (Patrón de diseño similar a MVC/MVP):


```text
+-------------------------------------------------------+
|                  Capa de Vista (gui.py)               |
|-------------------------------------------------------|
|  - Ventana principal de Tkinter                       |
|  - Captura de eventos de ratón y teclado              |
|  - Renderizado de componentes visuales                |
|    (Botones / Labels)                                 |
+-------------------------------------------------------+
                         |
                         | Eventos de usuario
                         v
+-------------------------------------------------------+
|                 Capa de Lógica (core.py)              |
|-------------------------------------------------------|
|  - Clase CalculadoraEngine                            |
|  - Control de estados y memoria                       |
|  - Operaciones matemáticas puras                      |
+-------------------------------------------------------+
```


### Ventajas de este diseño:
1. **Mantenibilidad:** Si se desea cambiar Tkinter por PyQt o una interfaz web, la lógica interna (`core.py`) no sufre ningún cambio.
2. **Testabilidad:** El motor matemático se prueba sin necesidad de levantar ventanas gráficas ni simular clics.
