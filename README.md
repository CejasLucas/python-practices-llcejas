# Proyecto personal en Python 

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)

¡Bienvenido! Este es mi repositorio personal donde pongo en práctica mis habilidades como programador.  
Este proyecto está dirigido a estudiantes y autodidactas que desean mejorar su comprensión práctica de **Python**.

Aquí encontrarás ejercicios, scripts y utilidades que exploran tanto lo básico como aspectos más avanzados del lenguaje.

Este proyecto tiene como objetivo **reforzar y organizar mi aprendizaje** en programación con Python, usando una estructura 
modular que facilita la escalabilidad, la reutilización de código y el uso de buenas prácticas.

---

## 🧰 Tecnologías y librerías principales

### Lenguaje y estructuras de control:

- Bucles `for` y `while`
- Condicionales (`if`, `else`, `elif`)
- Métodos y clases (`def`, `class`) 
- Colecciones como `list`, `dict`, `set`, `tuple`

### Herramientas y librerías:
1. **Sistema de Archivos:**
    - `os:` Navegación de directorios, manipulación de rutas, lectura de variables de entorno

2. **Análisis de Datos:**
   - `matplotlib:` Visualización de datos con gráficos de barras, líneas, tortas (pie charts).
   - `matplotlib_venn:` Diagramas de dos conjuntos (venn2) y tres conjuntos (venn3). Incluyendo operaciones
      con conjuntos como union, intersection y difference.
   - `pandas:` Manejo y análisis de datos usando estructuras Series y DataFrame.
   - `numpy:` Operaciones con matrices y arreglos multidimensionales.
   - `networkx:` Algoritmos en grafos (Djikstrack).

3. **Desarrollo web:**

    - `Flask + Flask-SocketIO` para backend.
    - `JavaScript + HTML + CSS` para frontend.
    - `Blueprint` para organizar vistas y rutas. 
    - Terminal interactiva con `xterm.js`.
    - Librerías auxiliares para ejecución de código en vivo:
      - `queue | threading:` Ejecución en segundo plano y sincronización
      - `importlib:` Carga dinámica de módulos 
      - `io | sys:` Redirección de entrada/salida estándar 
      - `base64:` Codificación y decodificación de datos 
      - `builtins:` Acceso a funciones y objetos integrados de Python

[NOTA] Todo está organizado por carpetas para facilitar la navegación, el mantenimiento y la extensión del repositorio.

---

## 🧱 Breve resumen de la aplicación

Cada subdirectorio de src/main/ representa un módulo temático y contiene:
- Dentro del package **Practices** vamos a tener cada módulo que contendrá:
  - `exerciseN.py:` Ejercicios específicos de ese módulo.
  - `__main__.py:` Punto de entrada principal del módulo.
  - `__menu__.py:` Menú con un breve enunciado sobre qué hace cada ejercicio.
  - `__init__.py:` Necesario para que el directorio sea tratado como un paquete.


- Dentro de **WebApp** se encuentra una aplicación web desarrollada con **Flask y SocketIO**, 
que permite ejecutar y visualizar ejercicios desde el navegador con una terminal 
interactiva integrada (basada en **xterm.js**). Está diseñada para facilitar pruebas, 
depuración y ejecución dinámica de código Python.

---
## 📈 Arquitectura del proyecto

``` bash
.
├── .venv/                     # Entorno virtual local (excluido por .gitignore)
├── data/                      # Archivos de datos (txt, csv) para análisis y gráficos
├── lib/
├── src/                       # Código fuente principal
│   ├── main/
│   │   ├── Practices/         # Funciones reutilizables
│   │   │   ├── conditionals/
│   │   │   ├── cycle_for/
│   │   │   ├── cycle_while/
│   │   │   ├── dictionaries/
│   │   │   ├── lists/
│   │   │   ├── sets/
│   │   │   ├── tuples/
│   │   │   ├── utils_matplotlib/
│   │   │   ├── utils_networkx/
│   │   │   ├── utils_numpy/
│   │   │   ├── utils_pandas/
│   │   │   ├── utils_venn_diagrams/
│   │   │   ├── __loader__.py
│   │   │   └── __init__.py
│   │   └── WebApp/            # Aplicación web
│   │       ├── static/  
│   │       │    ├── javascript/
│   │       │    ├── style/
│   │       │    └── xterm/   # Terminal interactiva en navegador
│   │       ├── templates/     # Archivos HTML
│   │       ├── app.py         # Configuración principal de Flask
│   │       ├── module.py      # Lógica de módulos
│   │       ├── routes.py      # Rutas y endpoints
│   │       ├── socketio_handlers.py # Manejo de eventos en tiempo real
│   │       └── __init__.py
│   └── test/                      
│       ├── test.py
│       └── __init__.py
├── .gitignore                 # Ignora archivos como .venv/
└── README.md                  # Documentación del proyecto
```
---

## 📦 `__init__.py`: ¿Qué es y por qué importa?

Este archivo convierte una carpeta en un **paquete de Python**. Aunque en versiones recientes no es obligatorio, se recomienda incluirlo por:

- Organización del código
- Compatibilidad retroactiva 
- Importaciones controladas
- Permite ejecutar con `python -m` sin errores

Incluso si el archivo está vacío, su presencia mejora la claridad y el mantenimiento del proyecto.

---

## 🔧 Configuración del entorno virtual

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

## ⚙️ `python3 -m`: ¿Cómo ejecuto los módulos desde la terminal?

Desde la **raíz del proyecto**, donde se encuentran: 
[`.gitignore`, `.venv`, `src`, `README.md`], podés ejecutar cualquier módulo usando:
```bash
  python3 -m src.main.nombre_modulo
```
Ejemplo:
```bash
   python3 -m src.main.utils_pandas
```

---

## 🌐 `python3 -m`:  ¿Cómo correr la WebApp desde la terminal?

La aplicación web se encuentra en el módulo WebApp y está construida 
con Flask y Flask-SocketIO. Esta app permite ejecutar ejercicios desde 
el navegador mediante una terminal interactiva basada en xterm.js. 
Para levantar la WebApp, desde la raíz del proyecto, ejecutá:
```bash
   python3 -m src.main.WebApp
```

Esto iniciará el servidor Flask, que por defecto corre en:
> Running on http://localhost:5000 \
> Press CTRL+C to quit

###  ¿Qué vas a ver en el navegador? 
- Un menú de ejercicios disponibles 
- Una terminal interactiva (basada en xterm.js)
- La posibilidad de ejecutar código en vivo desde el navegador
---

## 👨‍💻 _Autor: Lucas Leonel Cejas_

Técnico Universitario en Programación Informática.  
Apasionado por el aprendizaje continuo, la mejora progresiva y el código bien estructurado.

📬 ¿Sugerencias o mejoras?  
¡Sos bienvenido a abrir un issue o enviar un pull request para colaborar!