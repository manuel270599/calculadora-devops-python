# Pipeline de CI/CD con GitHub Actions

Este proyecto cuenta con una canalización de Integración Continuada y Despliegue Continuo (CI/CD) definida en `.github/workflows/ci.yml`.

## Flujo del Pipeline (Workflows)

```text
             [ Push / PR a main ]
                       |
                       v
          1. Checkout del código
                       |
                       v
       2. Configuración del entorno
                  Python 3.11
                       |
                       v
       3. Instalación de dependencias
               (requirements.txt)
                       |
                       v
       4. Ejecución de Pruebas Unitarias
                    (pytest)
                       |
              ┌────────┴────────┐
              |                 |
           ¿Pasan?             NO
              |                 |
             SÍ                 v
              |         Pipeline detenido
              v
       5. Empaquetado con PyInstaller
          (Generación del ejecutable)
                       |
                       v
       6. Publicación del Ejecutable
          como Artefacto en GitHub

## Beneficios
* **Calidad Garantizada:** Ninguna versión con fallos en el motor matemático se empaqueta.
* **Entregables Automáticos:** No es necesario compilar manualmente el ejecutable en la máquina local.
