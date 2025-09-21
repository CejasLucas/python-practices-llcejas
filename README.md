# 🐍 Proyecto personal en Python

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)

¡Bienvenido! Este es mi repositorio personal donde pongo en práctica mis habilidades como programador. 
Este proyecto está dirigido a estudiantes y autodidactas que desean mejorar su comprensión práctica de **Python**.

Aquí encontrarás ejercicios, scripts y utilidades que exploran tanto lo básico como aspectos más avanzados del lenguaje.

Este proyecto tiene como objetivo **reforzar y organizar mi aprendizaje** en programación con Python, usando una estructura 
modular que facilita la escalabilidad, la reutilización de código y el uso de buenas prácticas.

## 📂 Contenido del repositorio

- Ejercicios prácticos por tema (condicionales, ciclos, colecciones, diagramas de Venn, etc.)
- Scripts para automatización y scripting
- Contenido avanzado como análisis de datos y grafos

Todo está organizado por carpetas para facilitar la navegación, el mantenimiento y la extensión del repositorio.

---

## 🧰 Temas y herramientas

### Lenguaje y estructuras de control:

- Bucles `for` y `while`
- Condicionales (`if`, `else`, `elif`)
- Métodos y clases (`def`, `class`) 
- Colecciones como `list`, `dict`, `set`, `tuple`

### Herramientas y librerías:

- Automatización con scripts  
- Análisis de datos con:
  - `matplotlib`: Visualización de datos con gráficos de **barras, líneas, tortas (pie charts).**
  - `matplotlib_venn`: Diagramas de dos conjuntos (venn2) y tres conjuntos (venn3). Incluyendo operaciones 
    con conjuntos como **union, intersection y difference.**  
  - `pandas`: Manejo y análisis de datos usando estructuras **Series** y **DataFrame**  
  - `numpy`: Operaciones con **matrices** y arreglos multidimensionales  
  -  `networkx`: Algoritmos en grafos (Djikstrack)

---

## 📁 Estructura del Proyecto

Cada subdirectorio de `src/main/` representa un módulo temático y contiene:

- `exerciseN.py`: Ejercicios específicos de ese tema.
- `__main__.py`: Punto de entrada principal del módulo.
- `__init__.py`: Necesario para que el directorio sea tratado como un paquete.

```bash
.
├── .venv/                     # Entorno virtual local (excluido por .gitignore)
├── data/                      # Archivos de datos (txt, csv) para análisis y gráficos
├── src/                       # Código fuente principal
│   └── main/
│       ├── __utils__/         # Funciones auxiliares reutilizables
│       │   ├── __init__.py
│       │   └── ExerciseBuilder.py
│       ├── conditionals/
│       ├── cycle_for/
│       ├── cycle_while/
│       ├── dictionaries/
│       ├── lists/
│       ├── sets/
│       ├── tuples/
│       ├── utils_matplotlib/
│       ├── utils_networkx/
│       ├── utils_numpy/
│       ├── utils_pandas/
│       └── utils_venn_diagrams/
├── test/                      # Pruebas automáticas
│   ├── __init__.py
│   └── test.py
├── .gitignore                 # Ignora archivos como .venv/
└── README.md                  # Documentación del proyecto
```

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
  python3 -m src.main.nombre_modulo
```

Ejemplo:
```bash
   python3 -m src.main.utils_pandas
```

---

## 👨‍💻 _Autor: Lucas Leonel Cejas_

Técnico Universitario en Programación Informática.  
Apasionado por el aprendizaje continuo, la mejora progresiva y el código bien estructurado.

📬 ¿Sugerencias o mejoras?  
¡Sos bienvenido a abrir un issue o enviar un pull request para colaborar!