#  Calculadora Desktop Nativa (DevOps-Driven)

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-blue?style=for-the-badge)
![pytest](https://img.shields.io/badge/Testing-pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)

Aplicación de escritorio de calculadora estilo sistema operativo (Windows nativo), construida en Python aplicando **Clean Architecture** y un ciclo **DevOps completo** (Pruebas unitarias automatizadas y empaquetado CI/CD).

---

##  Documentación del Proyecto
* [Project Charter / Acta de Constitución](docs/project-charter.md)
* [Arquitectura de Software](docs/architecture.md)

---

## 🚀 Hoja de Ruta (Sprints)
- [x] **Sprint 1:** Motor Matemático (Core) & Cobertura de Pruebas $100\%$.
- [x] **Sprint 2:** Interfaz Gráfica Responsiva (Tkinter) & Atajos de Teclado.
- [x] **Sprint 3:** Pipeline CI/CD con GitHub Actions & Generación del Ejecutable.

---

##  Instrucciones de Ejecución Local

```bash
# Clonar el repositorio
git clone [https://github.com/TU_USUARIO/calculadora-devops-python.git](https://github.com/TU_USUARIO/calculadora-devops-python.git)
cd calculadora-devops-python

# Crear entorno virtual e instalar dependencias
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt

# Ejecutar la aplicación
python src/gui.py

# Ejecutar pruebas unitarias
pytest
```