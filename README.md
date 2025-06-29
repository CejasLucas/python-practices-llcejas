# 🐍 Repositorio de Práctica en Python

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)

¡Bienvenido! Este es mi repositorio personal donde pongo en práctica mis habilidades como programador utilizando **Python**.  
Este proyecto está dirigido a estudiantes y autodidactas que desean mejorar su comprensión práctica de Python.

Aquí encontrarás ejercicios, scripts, proyectos y utilidades que exploran tanto lo básico como aspectos más avanzados del lenguaje.

Este proyecto tiene como objetivo **reforzar y organizar mi aprendizaje** en programación con Python,  
usando una estructura modular que facilita la escalabilidad, la reutilización de código y el uso de buenas prácticas.

## 📂 Contenido del repositorio

- Ejercicios prácticos por tema (condicionales, ciclos, colecciones, diagramas de Venn, etc.)
- Scripts para automatización y scripting
- Proyectos y utilidades
- Contenido avanzado como análisis de datos y grafos

Todo está organizado por carpetas para facilitar la navegación, el mantenimiento y la extensión del repositorio.

---

## 🧰 Temas y herramientas

### Lenguaje y estructuras de control:

- Bucles `for` y `while`
- Condicionales (`if`, `else`, `elif`)
- Métodos y clases (`def`, `class`) 
- Colecciones como `list`, `dict`, `set`, `tuple`
- Operaciones con conjuntos y diagramas de Venn: `union`, `intersection`, `difference` 

### Herramientas y librerías:

- Automatización con scripts
- Análisis de datos con `pandas`, `numpy`, `matplotlib` (próximamente)
- Algoritmos en grafos usando `networkx`

---

## 📁 Estructura del Proyecto

Cada subdirectorio de `src/main/` representa un módulo temático y contiene:

- `exerciseN.py`: Ejercicios específicos de ese tema.
- `__main__.py`: Punto de entrada principal del módulo.
- `__init__.py`: Necesario para que el directorio sea tratado como un paquete.

```bash
.
├── .venv/                  # Entorno virtual local (excluido por .gitignore)
├── src/                    # Código fuente principal
│   └── main/
│       ├── __utils__/      # Funciones auxiliares reutilizables
│       │   ├── __init__.py
│       │   └── builder.py
│       ├── conditionals/
│       ├── cycle_for/
│       ├── cycle_while/
│       ├── dictionaries/
│       ├── lists/
│       ├── sets/
│       ├── tuples/
│       ├── utils_matplotlib/
│       ├── utils_pandas/
│       └── utils_venn_diagrams/
├── test/                   # Pruebas automáticas
│   ├── __init__.py
│   └── test.py
├── .gitignore              # Ignora archivos como .venv/
└── README.md               # Documentación del proyecto
```

--- 

## 📥 Importaciones correctas en proyectos Python

Cuando se trabaja con proyectos estructurados como este, es fundamental usar **importaciones absolutas**, desde la raíz del proyecto.

✅ Correcto:
```python
from src.main.__utils__.builder import ExerciseBuilder
from src.main.conditionals.exercise1 import run_exercise
```

❌ Incorrecto (puede causar errores):
```python
from ..__utils__ import builder
from conditionals.exercise1 import run_exercise
```

Usar `python -m` desde la raíz requiere importaciones absolutas para que Python sepa cómo encontrar los módulos.

---

## 🔧 Configuración del entorno virtual en Ubuntu

Para evitar conflictos entre dependencias y mantener el proyecto aislado del sistema, se recomienda usar un entorno virtual.  
Una vez activado, todos los paquetes que instales con `pip` quedarán guardados dentro de `.venv/`.

> 📝 El directorio `.venv/` no debe subirse al repositorio, por eso se incluye en `.gitignore`.

1. **Crear el entorno virtual:**

    ```bash
    python3 -m venv .venv
    ```

2. **Activar el entorno virtual:**

    ```bash
    source .venv/bin/activate
    ```

3. **Instalar dependencias:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Guardar dependencias (opcional):**

    ```bash
    pip freeze > requirements.txt
    ```

---

## 📦 `__init__.py`: ¿Qué es y por qué importa?

Este archivo convierte una carpeta en un **paquete de Python**. Aunque en versiones recientes no es obligatorio, se recomienda incluirlo por:

- Organización del código
- Compatibilidad retroactiva 
- Importaciones controladas
- Permite ejecutar con `python -m` sin errores

Incluso si el archivo está vacío, su presencia mejora la claridad y el mantenimiento del proyecto.

### ¿Cómo ejecuto los módulos del proyecto?

Desde la **raíz del proyecto** (donde se encuentran `.gitignore`, `.venv`, `src`, `README.md`), podés ejecutar cualquier módulo usando:

```bash
  python -m src.main.nombre_modulo
```

Ejemplo:
```bash
  python -m src.main.conditionals
```

---

## 👨‍💻 _Autor: Lucas Leonel Cejas_

Técnico Universitario en Programación Informática.  
Apasionado por el aprendizaje continuo, la mejora progresiva y el código bien estructurado.

📬 ¿Sugerencias o mejoras?  
¡Sos bienvenido a abrir un issue o enviar un pull request para colaborar!