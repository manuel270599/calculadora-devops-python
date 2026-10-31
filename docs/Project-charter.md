#  Project Charter: Calculadora Desktop Nativa (DevOps-Driven)

## 1. Nombre del Proyecto y Repositorio

- **Nombre del Proyecto:** Calculadora Desktop estilo Windows
- **Nombre del Repositorio:** `calculadora-devops-python`
- **Tecnología Principal:** Python 3.11+ (Tkinter)

## 2. Objetivo del Proyecto

Desarrollar una aplicación de escritorio multiplataforma de calculadora que reproduzca exactamente la experiencia visual y funcional de la calculadora nativa de un sistema operativo (estilo Windows 10/11), aplicando **Clean Architecture** (separación estricta entre interfaz y lógica) y un flujo de trabajo **DevOps automatizado (CI/CD)**.

## 3. Alcance del Proyecto (Scope)

### Incluido (In-Scope)

- **Operaciones Básicas:** Suma, resta, multiplicación y división con soporte para operaciones encadenadas inmediatas (ej. `5 + 3 =` y luego `* 2 =`).
- **Operaciones Rápidas (Un solo botón):** Porcentaje (`%`), Raíz cuadrada (`√x`), Cuadrado (`x²`), Inverso (`1/x`) y Cambio de signo (`±`).
- **Entradas y Atajos:** Uso mediante clics en pantalla y soporte nativo para el teclado numérico (`0-9`, `+`, `-`, `*`, `/`, `Enter`, `Backspace`, `Escape`).
- **Control de Borrado y Estado:** Botones de Limpiar Todo (`C`), Limpiar Entrada (`CE`) y Borrar último carácter (`⌫`).
- **Pantalla de Historial Auxiliar:** Indicador en la parte superior que muestra la operación parcial realizada.
- **DevOps & CI/CD:**
  - Pruebas unitarias automáticas con `pytest` ejecutadas en cada *Push* o *Pull Request*.
  - Generación de un archivo ejecutable estandarizado (`.exe` para Windows o binario para Linux) descargable desde GitHub Actions.

### No Incluido (Out-of-Scope)

- Modo calculadora científica avanzada (funciones trigonométricas, logaritmos, matrices).
- Conexión a bases de datos o servicios en la nube (el estado es local e instantáneo).

## 4. Arquitectura del Software (Clean Architecture)

El proyecto se dividirá en dos capas independientes:

```text
                  +-----------------------------------+
                  |   Capa de Presentación (gui.py)   |
                  |  - Interfaz Tkinter / Atajos      |
                  +-----------------------------------+
                                    |
                                    v (Llama a métodos)
                  +-----------------------------------+
                  |  Capa de Lógica/Core (core.py)    |
                  |  - CalculadoraEngine / Estados    |
                  +-----------------------------------+
```

- **`core.py` (Capa de Negocio):** No importa ninguna librería de interfaz gráfica. Procesa números, almacena el operador actual, maneja la memoria temporal y ejecuta los cálculos. Es 100 % testeable.
- **`gui.py` (Capa de Vista):** Captura los clics o teclas, actualiza la pantalla y le delega el procesamiento matemático a `core.py`.

## 5. Definición de Sprints (Metodología DevOps)

| Sprint | Nombre | Actividades principales | Entregables |
|:---:|---|---|---|
| **Sprint 1** | Lógica Base y Pruebas Unitarias | - Implementación de la clase `CalculadoraEngine`.<br>- Desarrollo de operaciones matemáticas.<br>- Gestión de estados y operaciones encadenadas.<br>- Implementación de pruebas con `pytest`. | - `src/core.py`<br>- `tests/test_core.py`<br>- Cobertura del 100 % del Core. |
| **Sprint 2** | Interfaz Gráfica y UX | - Diseño de la interfaz con `Tkinter`.<br>- Implementación del diseño mediante `grid layout`.<br>- Integración de eventos del teclado.<br>- Vinculación de la interfaz con el Core. | - `src/gui.py`<br>- Calculadora funcional.<br>- Interfaz gráfica estilo Windows 10/11. |
| **Sprint 3** | CI/CD Pipeline y Empaquetado | - Configuración de GitHub Actions.<br>- Creación del workflow `.github/workflows/ci.yml`.<br>- Automatización de pruebas con `pytest`.<br>- Empaquetado con `PyInstaller`.<br>- Publicación de ejecutables y documentación. | - Workflow CI/CD funcional.<br>- Ejecutable `.exe` para Windows.<br>- Artefactos descargables desde GitHub Actions.<br>- Documentación del repositorio. |

## 6. Criterios de Aceptación (Definition of Done - DoD)

1. **Calidad de Código:** El 100 % de las pruebas unitarias pasan sin errores antes de fusionar código a la rama principal (`main`).
2. **Usabilidad:** La calculadora permite realizar la secuencia completa de operaciones usando tanto el ratón como el teclado.
3. **Automatización:** Cada `git push` a `main` genera automáticamente el ejecutable listo para ser descargado y ejecutado sin requerir tener Python instalado.
