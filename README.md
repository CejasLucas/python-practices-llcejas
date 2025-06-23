# 🐍 Repositorio de Práctica en Python

¡Bienvenido! Este es mi repositorio personal donde pongo en práctica mis habilidades como programador utilizando **Python**. Aquí encontrarás ejercicios, scripts, proyectos y utilidades que exploran tanto lo básico como aspectos más avanzados del lenguaje.

Este proyecto tiene como objetivo **reforzar y organizar mi aprendizaje** en programación con Python, usando una estructura modular que facilita la escalabilidad, la reutilización de código y el uso de buenas prácticas.

### ¿Qué encontrarás en este repositorio?

- Ejercicios prácticos por tema (condicionales, ciclos, colecciones, diagramas de venn etc.)
- Scripts para automatización y scripting
- Proyectos y utilidades
- Contenido avanzado como análisis de datos y grafos

Todo está organizado por carpetas para facilitar la navegación, el mantenimiento y la extensión del repositorio.

---

## 🧰 Temas y herramientas

### Lenguaje y estructuras de control:

- Bucles `for` y `while`
- Condicionales (`if`, `else`, `elif`)
- Metodos y clases (`def`, `class`) 
- Colecciones como `list`, `dict`, `set`, `tuple`
- Operaciones diagramas de venn `union`, `intersection`, `diference` 

### Herramientas y librerías:

- Automatización con scripts
- Análisis de datos con `pandas`, `numpy`, `matplotlib` (próximamente)
- Algoritmos en grafos usando `networkx`

---

## 📁 Estructura del Proyecto
- Cada subdirectorio de src/main/ representa un módulo temático y contiene:

- **exerciseN.py:** Ejercicios específicos de ese tema.

- **__ main __.py:** Punto de entrada principal del módulo.

- **__ init __.py:**  Necesario para que el directorio sea tratado como un paquete.


```bash
.
├── .venv/                  # Entorno virtual local (excluido por .gitignore)
├── src/                    # Código fuente principal
│   └── main/
│       ├── __utils__/      # Funciones auxiliares reutilizables
│       │   ├── __init__.py
│       │   └── builder.py
│       ├── conditionals/   # Ejercicios con condicionales
│       │   ├── __init__.py
│       │   ├── __main__.py
│       │   ├── exercise1.py
│       │   └── exerciseN.py
│       ├── cycle_for/      # Ejercicios con bucles for
│       │   ├── __init__.py
│       │   ├── __main__.py
│       │   ├── exercise1.py
│       │   └── exerciseN.py
│       ├── cycle_while/    # Ejercicios con bucles while
│       │   ├── __init__.py
│       │   ├── __main__.py
│       │   ├── exercise1.py
│       │   └── exerciseN.py
│       ├── dictionaries/   # Ejercicios con diccionarios
│       │   ├── __init__.py
│       │   ├── __main__.py
│       │   ├── exercise1.py
│       │   └── exerciseN.py
│       ├── lists/          # Ejercicios con listas
│       │   ├── __init__.py
│       │   ├── __main__.py
│       │   ├── exercise1.py
│       │   └── exerciseN.py
│       ├── sets/           # Ejercicios con conjuntos
│       │   ├── __init__.py
│       │   ├── __main__.py
│       │   ├── exercise1.py
│       │   └── exerciseN.py
│       ├── tuples/         # Ejercicios con tuplas
│       │   ├── __init__.py
│       │   ├── __main__.py
│       │   ├── exercise1.py
│       │   └── exerciseN.py
│       ├── venn_diagrams/  # Operaciones con conjuntos
│       │   ├── __init__.py
│       │   ├── __main__.py
│       │   ├── exercise1.py
│       │   └── exerciseN.py
│       └── __init__.py         # Inicializa el paquete
├── test/                       # Pruebas automáticas
│   ├── __init__.py
│   └── test.py
├── .gitignore              # Ignora archivos como .venv/
└── README.md               # Documentación del proyecto
```
--- 

## 📦 `__init__.py`: ¿Qué es y por qué importa?

Este archivo convierte una carpeta en un **paquete de Python**. Aunque en versiones recientes no es obligatorio, se recomienda incluirlo por:
- **Organización del código**
- **Compatibilidad retroactiva** 
- **Importaciones controladas**
- Permite ejecutar con **python -m** sin errores
- Incluso si el archivo está vacío, su presencia mejora la claridad y el mantenimiento del proyecto.

¿Cómo ejecuto los módulos del proyecto?
Desde la **raíz del proyecto** (donde se encuentran `.gitignore`, `.venv`, `src`, `README.md`), podés ejecutar cualquier módulo usando:
``` bash 
    -m src.main.<nombre_modulo>
```
---

## 📥 Importaciones correctas en proyectos Python
Cuando se trabaja con proyectos estructurados como este, es fundamental usar importaciones absolutas. Es decir, desde la raíz del proyecto hacia adentro.

✅ Correcto:

``` python 
    from src.main.__utils__.builder import ExerciseBuilder
    from src.main.conditionals.exercise1 import run_exercise
```

 Incorrecto (puede causar errores):

``` python 
    from ..__utils__ import builder
    from conditionals.exercise1 import run_exercise
```
Usar python -m desde la raíz requiere importaciones absolutas para que Python sepa cómo encontrar los módulos.

🐧 Configuración del entorno virtual en Ubuntu
Para aislar las dependencias del proyecto y evitar conflictos con otros entornos de Python del sistema, es altamente recomendado usar un entorno virtual.

🔧 1. Crear el entorno virtual
Desde la raíz del proyecto, ejecutá:

bash
Copiar
Editar
python3 -m venv .venv
Esto crea una carpeta .venv/ que contiene una instalación aislada de Python.

▶️ 2. Activar el entorno virtual
En Ubuntu/Linux:

bash
Copiar
Editar
source .venv/bin/activate
Verás que el prompt de tu terminal cambia para reflejar el entorno activado, por ejemplo:

ruby
Copiar
Editar
(.venv) usuario@ubuntu:~/proyecto$
📦 3. Instalar dependencias
Si existe un archivo requirements.txt, podés instalar las dependencias con:

bash
Copiar
Editar
pip install -r requirements.txt
Para guardar las librerías que estás usando:

bash
Copiar
Editar
pip freeze > requirements.txt
El directorio .venv/ no debe subirse al repositorio, por eso se incluye en .gitignore.

💡 ¿Qué es PyCharm y cómo usarlo?
PyCharm es un entorno de desarrollo (IDE) especializado para Python. Ideal para este tipo de proyectos gracias a:

Autocompletado inteligente y navegación de código.

Soporte para entornos virtuales (.venv).

Integración con Git.

Depurador gráfico y herramientas para testing.

Para configurar tu proyecto en PyCharm:
Abrí PyCharm y seleccioná Open para abrir la carpeta del proyecto.

Ve a Settings > Project > Python Interpreter y seleccioná el entorno .venv creado.

Ejecutá scripts con clic derecho en __main__.py → Run.

🧼 Buenas prácticas
Estructura modular: cada tema en su carpeta.

Importaciones absolutas: evitan errores al ejecutar desde la raíz.

Entorno virtual: mantiene tu entorno limpio y reproducible.

__init__.py en cada paquete: asegura que las importaciones funcionen correctamente.

README bien documentado: facilita compartir el proyecto y mantenerlo actualizado.

👨‍💻 Autor
Lucas Leonel Cejas
Estudiante y entusiasta de la programación. Apasionado por el aprendizaje continuo, la mejora progresiva y el código bien estructurado.

📬 ¿Sugerencias o mejoras?
¡Sos bienvenido a abrir un issue o enviar un pull request para colaborar!