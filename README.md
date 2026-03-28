# U1 Interfaz Grafica De Usuario
## Introducción

Las Interfaces Gráficas de Usuario (GUI, por sus siglas en inglés: Graphical User Interface) representan un elemento esencial en el desarrollo de software moderno, ya que permiten la interacción entre el usuario y los sistemas informáticos mediante componentes visuales como botones, ventanas, menús e iconos. Estas interfaces tienen como objetivo principal mejorar la usabilidad y accesibilidad de las aplicaciones, facilitando su uso incluso para personas sin conocimientos técnicos avanzados.

En la actualidad, el desarrollo de interfaces gráficas ha evolucionado hacia la creación de aplicaciones multiplataforma, capaces de ejecutarse en distintos sistemas operativos sin necesidad de reescribir el código base. En este contexto, herramientas como Flet, un framework basado en Python, permiten diseñar interfaces gráficas interactivas mediante una amplia biblioteca de controles predefinidos inspirados en Flutter. Esto simplifica el proceso de desarrollo y reduce la complejidad técnica al evitar el uso de lenguajes adicionales como Dart.

Asimismo, el uso de frameworks multiplataforma contribuye a optimizar el tiempo de desarrollo y a garantizar una experiencia de usuario consistente en dispositivos móviles y de escritorio. Flet destaca por su capacidad de integrar librerías externas relevantes como NumPy y Pandas, lo que permite ampliar las funcionalidades de las aplicaciones desarrolladas y transformar conceptos teóricos de programación en soluciones prácticas y versátiles.

Por lo tanto, el estudio de las interfaces gráficas de usuario, junto con el análisis de herramientas modernas como Flet, resulta fundamental para comprender cómo se diseñan y desarrollan aplicaciones interactivas, eficientes y adaptables a diferentes entornos tecnológicos.

### 1.1 Creación de Interfaz Gráfica para Usuario

#### Introducción

La creación de una interfaz gráfica de usuario (GUI) es un proceso esencial en el desarrollo de aplicaciones modernas, ya que permite establecer una comunicación visual e interactiva entre el usuario y el sistema informático. A través de componentes como botones, menús, cuadros de texto y ventanas, las GUI facilitan el uso de los programas, mejorando la accesibilidad y la comprensión de las funcionalidades disponibles. En el contexto actual, donde se busca que las aplicaciones sean intuitivas y eficientes, el diseño de interfaces gráficas se ha convertido en un área clave dentro de la ingeniería de software.

#### Desarrollo

El desarrollo de una interfaz gráfica de usuario implica diversas etapas que van desde la planificación del diseño hasta la implementación técnica de los elementos visuales. En primer lugar, se deben considerar los principios de usabilidad y experiencia de usuario, los cuales buscan que la interacción sea clara, coherente y sencilla. Esto implica organizar adecuadamente los componentes gráficos, mantener consistencia en los estilos visuales y asegurar que las acciones del usuario generen respuestas comprensibles dentro del sistema.

Actualmente, el uso de frameworks multiplataforma ha simplificado el proceso de creación de interfaces gráficas, permitiendo desarrollar aplicaciones que funcionan tanto en dispositivos móviles como en equipos de escritorio con un solo código base. Un ejemplo destacado es el framework Flet, el cual permite a los programadores trabajar con Python para diseñar interfaces interactivas mediante controles predefinidos basados en Flutter. Esta característica reduce la complejidad técnica, ya que no es necesario aprender lenguajes adicionales para lograr aplicaciones visuales modernas.

Como parte de la práctica realizada en clase, se llevó a cabo la creación de la interfaz gráfica de una calculadora, utilizando distintos componentes visuales como botones numéricos, operadores aritméticos y un campo de visualización de resultados. Esta actividad permitió aplicar los conceptos teóricos sobre diseño de interfaces, distribución de elementos y organización visual, así como comprender la importancia de una estructura clara para facilitar la interacción del usuario con la aplicación.

<img width="1920" height="1080" alt="Captura de pantalla 2026-02-07 102112" src="https://github.com/user-attachments/assets/ccbce3d6-69f5-4bc4-8454-e8b0d8c5302c" />


#### Conclusión

En conclusión, la creación de interfaces gráficas para usuario es un proceso fundamental que integra principios de diseño, programación y experiencia de usuario con el objetivo de facilitar la interacción con los sistemas informáticos. La elaboración de la interfaz gráfica de una calculadora durante la práctica permitió reforzar los conocimientos adquiridos y evidenciar la importancia de planificar adecuadamente la estructura visual de una aplicación. Por ello, comprender cómo se diseñan y desarrollan las GUI resulta indispensable para la construcción de software moderno, accesible y orientado a las necesidades reales de los usuarios.

### 1.2 Tipos de Eventos

#### Introducción

En el desarrollo de interfaces gráficas de usuario (GUI), los eventos representan las acciones que realiza el usuario o el sistema y que generan una respuesta dentro de la aplicación. Estos eventos son fundamentales para lograr la interactividad, ya que permiten que los componentes visuales reaccionen ante distintas acciones como clics, pulsaciones de teclas o cambios en los elementos de la interfaz. Comprender los tipos de eventos es esencial para diseñar aplicaciones dinámicas, funcionales y orientadas a la experiencia del usuario.

#### Desarrollo

Los eventos en una interfaz gráfica pueden clasificarse según el tipo de interacción que los origina. Uno de los más comunes es el evento de ratón, que incluye acciones como clic, doble clic, desplazamiento y movimiento del cursor sobre un componente. Estos eventos permiten ejecutar funciones específicas cuando el usuario interactúa directamente con los elementos visuales, como presionar un botón o seleccionar una opción en un menú.

Otro tipo importante son los eventos de teclado, que se generan cuando el usuario presiona o libera una tecla. Estos eventos son especialmente útiles en formularios, campos de texto y accesos rápidos dentro de la aplicación. Asimismo, existen los eventos de interfaz o de control, los cuales ocurren cuando se modifica el estado de un componente, por ejemplo, al cambiar el valor de un cuadro de texto, seleccionar una casilla o mover un control deslizante.

En el contexto del desarrollo multiplataforma con herramientas como Flet, los eventos permiten enlazar las acciones del usuario con funciones programadas en Python, facilitando la creación de aplicaciones interactivas con un solo código base. De esta manera, cada evento desencadena una respuesta lógica dentro del sistema, lo que contribuye a una experiencia de usuario más fluida y eficiente.

Como parte de la práctica realizada en clase, se implementó la funcionalidad de los botones de una calculadora, asignando eventos de clic a cada botón para ejecutar operaciones aritméticas básicas. Esta actividad permitió comprender de manera aplicada cómo los eventos controlan el comportamiento de los componentes gráficos y cómo se vinculan con la lógica del programa para responder a las acciones del usuario en tiempo real.

https://github.com/user-attachments/assets/7ec4c838-5721-4af0-977f-2e682c5cd24a

#### Conclusión

En conclusión, los tipos de eventos constituyen un elemento esencial en la programación de interfaces gráficas de usuario, ya que permiten gestionar la interacción entre el usuario y la aplicación. La correcta identificación y manejo de eventos como los de ratón, teclado y controles de interfaz posibilita el desarrollo de aplicaciones interactivas y funcionales. La práctica de implementar la funcionalidad de los botones en una calculadora reafirma la importancia de los eventos como mecanismo principal para controlar el comportamiento dinámico de una interfaz gráfica moderna.

### 1.3 Manejo de Eventos

#### Introducción

El manejo de eventos es un concepto fundamental en el desarrollo de interfaces gráficas de usuario (GUI), ya que permite que una aplicación responda de manera dinámica a las acciones realizadas por el usuario. Un evento se define como cualquier acción o suceso que ocurre dentro del sistema, como hacer clic en un botón, presionar una tecla o modificar el contenido de un campo de texto. La correcta gestión de estos eventos es esencial para lograr aplicaciones interactivas, funcionales y orientadas a la experiencia del usuario.

#### Desarrollo

El manejo de eventos consiste en detectar las acciones que realiza el usuario sobre los componentes de la interfaz gráfica y asociarlas a funciones o métodos que ejecuten una respuesta específica. Este proceso se conoce como programación dirigida por eventos, en la cual el flujo del programa depende de las interacciones del usuario y no únicamente de una secuencia lineal de instrucciones.

Entre los eventos más comunes se encuentran los eventos de ratón, que incluyen clic, doble clic y desplazamiento; los eventos de teclado, que se generan al presionar o soltar una tecla; y los eventos de cambio, que ocurren cuando se modifica el estado de un componente, como el contenido de un cuadro de texto o la selección de una opción en una lista. Cada uno de estos eventos puede ser capturado por el sistema y vinculado a una acción programada que determine el comportamiento de la aplicación.

En herramientas modernas para el desarrollo de interfaces gráficas, como Flet, el manejo de eventos se realiza mediante la asignación de funciones en Python a los diferentes controles visuales. Esto permite que cada interacción del usuario produzca una respuesta inmediata dentro de la aplicación, logrando una experiencia más fluida y eficiente. De esta forma, los eventos se convierten en el mecanismo principal para controlar la lógica y la interactividad de la interfaz gráfica.

#### Conclusión

En conclusión, el manejo de eventos es un elemento esencial en la programación de interfaces gráficas de usuario, ya que permite establecer una comunicación dinámica entre el usuario y el sistema. La adecuada identificación y programación de los distintos tipos de eventos garantiza que la aplicación responda de manera correcta a las acciones realizadas, mejorando la usabilidad y el rendimiento del software. Por ello, el dominio del manejo de eventos resulta indispensable para el desarrollo de aplicaciones interactivas y modernas.

### 1.4 Manejo de Componentes Gráficos de Control

#### Introducción

El manejo de componentes gráficos de control es un aspecto fundamental en el desarrollo de interfaces gráficas de usuario (GUI), ya que estos elementos permiten establecer la interacción directa entre el usuario y la aplicación. Los componentes de control incluyen elementos como botones, cuadros de texto, etiquetas, listas desplegables y controles deslizantes, los cuales facilitan la entrada de datos, la ejecución de acciones y la visualización de información dentro del sistema.

Comprender el funcionamiento y la manipulación de estos componentes es esencial para construir aplicaciones interactivas y funcionales, ya que cada uno cumple un propósito específico dentro de la interfaz y contribuye a mejorar la experiencia del usuario.

#### Desarrollo

El manejo de componentes gráficos de control implica su creación, configuración y programación para que respondan adecuadamente a las acciones del usuario. Cada componente posee propiedades que determinan su apariencia y comportamiento, tales como tamaño, color, posición, texto visible y estado de activación. Estas propiedades pueden modificarse para adaptar la interfaz a las necesidades del sistema y del usuario.

Además, los componentes de control se encuentran estrechamente relacionados con el manejo de eventos, ya que su funcionalidad depende de la respuesta que el programa ejecute cuando el usuario interactúa con ellos. Por ejemplo, un botón puede estar asociado a un evento de clic que ejecute una operación específica, mientras que un cuadro de texto permite capturar datos que posteriormente serán procesados por la aplicación.

En el desarrollo de aplicaciones multiplataforma con herramientas como Flet, los componentes gráficos se implementan mediante controles predefinidos que simplifican la construcción de interfaces visuales. Esto permite organizar los elementos de manera estructurada y asignarles funcionalidades mediante código en Python, logrando una integración eficiente entre la lógica del programa y la presentación visual. De esta manera, el manejo adecuado de los componentes de control garantiza interfaces coherentes, funcionales y fáciles de utilizar en diferentes entornos tecnológicos.

#### Conclusión

En conclusión, el manejo de componentes gráficos de control es un elemento clave para el desarrollo de interfaces gráficas de usuario, ya que permite definir la forma en que el usuario interactúa con la aplicación. La correcta configuración y programación de estos componentes asegura que la interfaz sea funcional, intuitiva y eficiente. Por ello, dominar el uso de los elementos gráficos de control resulta indispensable para el diseño de aplicaciones modernas que respondan de manera efectiva a las necesidades del usuario.

## Conclusión de la Unidad 1

En la Unidad 1 se abordaron los fundamentos relacionados con la creación y manejo de interfaces gráficas de usuario, destacando su importancia en el desarrollo de aplicaciones modernas orientadas a la interacción directa con el usuario. A lo largo de los temas estudiados, se comprendió que una GUI no solo cumple una función estética, sino que constituye un elemento clave para mejorar la usabilidad, accesibilidad y eficiencia de los sistemas informáticos.

Se analizaron aspectos esenciales como la creación de interfaces gráficas, el manejo de componentes de control y la gestión de eventos, los cuales permiten construir aplicaciones dinámicas y funcionales. Estos elementos trabajan de manera conjunta para establecer una comunicación efectiva entre el usuario y el sistema, respondiendo de forma adecuada a cada acción realizada dentro de la aplicación.

Asimismo, se reconoció la relevancia de herramientas modernas como Flet, que facilitan el desarrollo de interfaces gráficas multiplataforma mediante el uso de Python y controles visuales predefinidos. Esto permite transformar los conceptos teóricos en soluciones prácticas, optimizando el proceso de desarrollo y garantizando aplicaciones interactivas adaptables a distintos entornos tecnológicos.

En conclusión, el estudio de los fundamentos de las interfaces gráficas de usuario proporciona las bases necesarias para el diseño y desarrollo de aplicaciones modernas, destacando la importancia de integrar componentes visuales, eventos y principios de usabilidad. Estos conocimientos resultan indispensables para crear software eficiente, intuitivo y orientado a las necesidades reales de los usuarios.

## Referencias 

Autor desconocido. (2024). *Building multiplatform apps with Python and Flet* [Infografía]. Material proporcionado en clase.

Autor desconocido. (2024). *Framework Flet para el desarrollo de aplicaciones multiplataforma en Python* [Documento de apoyo]. Material proporcionado en clase.

Shneiderman, B., Plaisant, C., Cohen, M., Jacobs, S., Elmqvist, N., & Diakopoulos, N. (2016). Designing the user interface: Strategies for effective human-computer interaction (6th ed.). Pearson.

Preece, J., Rogers, Y., & Sharp, H. (2015). Interaction design: Beyond human-computer interaction (4th ed.). Wiley.

Flet. (2024). Build multi-platform apps in Python powered by Flutter. https://flet.dev

# U2 Interfaz Grafica De Usuario

##  Introducción

En la materia de **Tópicos Avanzados de Programación**, la Unidad 2: *Componentes y Librerías* aborda conceptos fundamentales para el desarrollo de software moderno, enfocados en la reutilización, modularidad y organización del código.

Los componentes permiten dividir una aplicación en partes más pequeñas, independientes y reutilizables, facilitando su mantenimiento y escalabilidad. Por otro lado, las librerías y paquetes proporcionan herramientas ya desarrolladas que ayudan a resolver problemas comunes, optimizando el tiempo de desarrollo y mejorando la calidad del software.

Durante esta unidad se analizan tanto las librerías proporcionadas por el lenguaje de programación como la creación de componentes y paquetes definidos por el usuario, lo que permite al desarrollador construir soluciones más eficientes, estructuradas y adaptables a distintos contextos.

El estudio de estos elementos es esencial para comprender cómo se diseñan sistemas modernos, donde la reutilización de código y el uso de herramientas externas son prácticas clave en la industria del software.

##  2.1 Definición conceptual de componentes, paquetes y librerías

En el desarrollo de software moderno, es fundamental comprender los conceptos de **componentes**, **librerías** y **paquetes**, ya que estos permiten organizar, reutilizar y estructurar el código de manera eficiente. Estos elementos forman la base de la programación modular, la cual facilita la creación de sistemas más escalables, mantenibles y comprensibles.

---

###  Componentes

Un **componente** es una unidad independiente de software que encapsula una funcionalidad específica y que puede ser reutilizada en diferentes partes de una aplicación o en distintos proyectos. Su principal objetivo es dividir un sistema en partes más pequeñas y manejables.

Los componentes pueden incluir tanto lógica de programación como elementos visuales, dependiendo del tipo de aplicación.

**Características principales:**
- Encapsulan funcionalidad específica  
- Son reutilizables  
- Tienen independencia respecto a otros componentes  
- Pueden configurarse mediante propiedades o parámetros  

**Tipos de componentes:**
- **Componentes visuales:** Son aquellos que tienen representación gráfica en la interfaz de usuario, como botones, formularios, menús o tablas.  
- **Componentes no visuales:** No tienen interfaz gráfica y se enfocan en la lógica del programa, como funciones, servicios, validaciones o controladores.  

El uso de componentes permite mejorar la organización del código, facilitar el mantenimiento y promover la reutilización en diferentes proyectos.

---

###  Librerías

Una **librería** es un conjunto de funciones, clases o módulos predefinidos que pueden ser utilizados por los desarrolladores para realizar tareas comunes sin tener que implementarlas desde cero.

Las librerías están diseñadas para resolver problemas específicos y pueden ser desarrolladas por terceros o formar parte del propio lenguaje de programación.

**Características:**
- Contienen código reutilizable  
- Facilitan el desarrollo de aplicaciones  
- Reducen la duplicación de código  
- Están enfocadas en resolver problemas específicos  

**Ejemplos de uso:**
- Manipulación de fechas  
- Operaciones matemáticas  
- Manejo de archivos  
- Desarrollo de interfaces gráficas  

El uso de librerías permite aumentar la productividad del desarrollador y mejorar la calidad del software, ya que muchas de ellas han sido ampliamente probadas y optimizadas.

---

###  Paquetes

Un **paquete** es una estructura que agrupa múltiples módulos, librerías o componentes relacionados en una sola unidad organizada. Su propósito es facilitar la distribución, instalación y mantenimiento del software.

Los paquetes suelen incluir no solo código, sino también archivos de configuración, documentación y dependencias necesarias para su funcionamiento.

**Características:**
- Organizan el código en estructuras jerárquicas  
- Facilitan la reutilización y distribución  
- Permiten gestionar dependencias  
- Mejoran la mantenibilidad del proyecto  

**Diferencia entre librería y paquete:**
- Una **librería** es un conjunto de funciones o clases enfocadas en una tarea específica  
- Un **paquete** es un contenedor que puede incluir una o varias librerías junto con otros recursos  

---

###  Importancia en el desarrollo de software

El uso de componentes, librerías y paquetes es esencial en la programación moderna debido a que:

- Permiten desarrollar aplicaciones más rápidas y eficientes  
- Mejoran la organización del código  
- Facilitan el trabajo colaborativo  
- Promueven la reutilización de soluciones ya existentes  
- Reducen errores al utilizar código probado  

---

###  Conclusión

Comprender la diferencia y el uso de componentes, librerías y paquetes es fundamental para cualquier desarrollador. Estos elementos permiten construir software más estructurado, reutilizable y escalable, siendo una base clave en el desarrollo de aplicaciones modernas y en el uso de frameworks y herramientas actuales.

Algunos ejemplos realizados a lo largo de la unidad son:

```python
import flet as ft
from dataclasses import dataclass

# Clase de datos (dataclass)
@dataclass
class Usuario:
    nombre: str
    rol: str
    color_borde: str = ft.Colors.BLUE


# Componente visual
class TarjetaPerfil(ft.Container):
    def __init__(self, usuario: Usuario):
        super().__init__()

        self.usuario = usuario

        self.content = ft.Column(
            controls=[
                ft.Text(usuario.nombre, weight=ft.FontWeight.BOLD, size=20),
                ft.Text(usuario.rol, italic=True),
                ft.ElevatedButton("Ver Perfil", on_click=self.saludar)
            ],
            tight=True
        )

        self.border = ft.border.all(2, usuario.color_borde)
        self.padding = 10
        self.border_radius = 10
        self.width = 200

    def saludar(self, e):
        print(f"Interactuando con el componente de {self.usuario.nombre}")


def main(page: ft.Page):
    page.title = "Unidad 2: Componentes con Dataclass"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Crear usuarios usando dataclass
    usuario1 = Usuario("Ana Garcia", "Desarrolladora Senior", ft.Colors.GREEN)
    usuario2 = Usuario("Carlos Ruiz", "Arquitecto de Software")

    # Crear tarjetas
    tarjeta1 = TarjetaPerfil(usuario1)
    tarjeta2 = TarjetaPerfil(usuario2)

    

    page.add(
        ft.Text("Lista de Usuarios", size=30, weight="bold"),
        ft.Row([tarjeta1, tarjeta2,], alignment=ft.MainAxisAlignment.CENTER)
    )


ft.app(target=main)
```
<img width="1584" height="892" alt="Captura de pantalla 2026-03-28 091204" src="https://github.com/user-attachments/assets/9a3c8c09-4300-4894-be77-4981f90e243f" />
Este programa crea una aplicación gráfica sencilla en Python donde se muestran tarjetas de perfil de usuarios.

En general, lo que hace es:

Define una estructura de datos para representar usuarios con nombre, rol y un color de borde.
Crea un componente visual reutilizable que muestra la información de cada usuario en forma de tarjeta.
Cada tarjeta incluye un botón que permite interactuar; al presionarlo, se genera un mensaje en la consola.
En la interfaz principal, se crean dos usuarios y se muestran sus tarjetas en pantalla, organizadas de forma horizontal.
Finalmente, ejecuta la aplicación para que todo se visualice en una ventana.

En resumen, el código demuestra cómo crear y usar componentes personalizados en una interfaz gráfica, aplicando reutilización de código y organización modular, que son conceptos clave de la unidad de Componentes y Librerías.

## 2.2 Uso de librerías proporcionadas por el lenguaje

En el desarrollo de software, los lenguajes de programación modernos incluyen un conjunto de herramientas predefinidas conocidas como **librerías estándar**. Estas librerías están diseñadas para facilitar la implementación de funcionalidades comunes, evitando que el desarrollador tenga que crear soluciones desde cero.

Las librerías proporcionadas por el lenguaje forman parte integral de su entorno de desarrollo y ofrecen módulos, funciones y clases que han sido previamente diseñados, probados y optimizados. Su uso es una práctica fundamental en la programación, ya que contribuye a mejorar la eficiencia, la calidad del código y la productividad.

---

### Concepto de librería estándar

Una **librería estándar** es un conjunto de recursos incluidos directamente en un lenguaje de programación que permite realizar tareas comunes como manejo de datos, operaciones matemáticas, manipulación de archivos, gestión de fechas, entre otras.

Estas librerías están disponibles sin necesidad de instalación adicional y cuentan con documentación oficial, lo que facilita su aprendizaje y aplicación.

---

### Importancia del uso de librerías del lenguaje

El uso de librerías estándar es esencial debido a las siguientes razones:

- Permiten reducir el tiempo de desarrollo al evitar la implementación de funcionalidades básicas.
- Ofrecen soluciones confiables, ya que han sido ampliamente probadas.
- Mejoran la legibilidad y mantenimiento del código.
- Promueven buenas prácticas de programación.
- Garantizan compatibilidad con el lenguaje y su entorno.

---

### Funcionalidades comunes de las librerías estándar

Las librerías proporcionadas por los lenguajes suelen incluir herramientas para:

- Operaciones matemáticas y estadísticas.
- Manejo de cadenas de texto.
- Entrada y salida de datos.
- Manipulación de archivos.
- Manejo de fechas y tiempo.
- Interacción con el sistema operativo.
- Estructuras de datos avanzadas.

---

### Ejemplos en diferentes lenguajes

#### Python

Python cuenta con una amplia librería estándar que incluye módulos como:

- `math`: permite realizar operaciones matemáticas avanzadas.
- `datetime`: facilita el manejo de fechas y horas.
- `os`: permite interactuar con el sistema operativo.
- `sys`: proporciona acceso a variables y funciones del sistema.

#### JavaScript

JavaScript incorpora objetos y funciones integradas como:

- `Math`: para operaciones matemáticas.
- `Date`: para manejo de fechas.
- `Array` y `String`: para manipulación de datos.
- `JSON`: para el manejo de datos estructurados.

---

### Ventajas del uso de librerías estándar

El uso de librerías proporcionadas por el lenguaje ofrece múltiples beneficios:

- Disminución de errores al utilizar código previamente validado.
- Mayor eficiencia en el desarrollo.
- Código más limpio y estructurado.
- Portabilidad entre diferentes sistemas.
- Acceso a documentación oficial y soporte de la comunidad.

---

### Consideraciones en su uso

Aunque las librerías estándar son herramientas muy útiles, es importante:

- Comprender su funcionamiento antes de utilizarlas.
- Evitar el uso innecesario de funciones que no aporten valor.
- Mantener el código claro y bien documentado.
- Elegir adecuadamente la librería según la necesidad del problema.

---

### Conclusión

El uso de librerías proporcionadas por el lenguaje es una práctica esencial en el desarrollo de software moderno. Estas herramientas permiten optimizar el tiempo de programación, mejorar la calidad del código y facilitar la resolución de problemas comunes. Su correcta utilización es una habilidad fundamental para cualquier desarrollador, ya que contribuye a la creación de aplicaciones más eficientes, mantenibles y robustas.

En clase se realizo el siguiente ejemplo:
```python
import matplotlib.pyplot as plt
import flet as ft
import flet_charts as fch
import random # Para simular datos de sensores

# --- FUNCIONES DE GRÁFICAS ---

def generar_grafica_barras():
    productos = ["A", "B", "C", "D"]
    ventas = [15, 30, 45, 10]
    fig, ax = plt.subplots(figsize=(4, 3), facecolor="#1e1e1e")
    ax.bar(productos, ventas, color="#4dabf7")
    ax.set_title("Ventas por Producto", fontsize=10, weight='bold', color="white")
    ax.set_facecolor("#1e1e1e")
    ax.tick_params(colors='white')
    plt.tight_layout()
    return fig

def generar_grafica_lineas():
    meses = ["Ene", "Feb", "Mar", "Abr", "May"]
    rendimiento = [10, 25, 18, 40, 35]
    fig, ax = plt.subplots(figsize=(4, 3), facecolor="#1e1e1e")
    ax.plot(meses, rendimiento, color="#ffa94d", marker='o', linewidth=2)
    ax.set_title("Tendencia de Rendimiento", fontsize=10, weight='bold', color="white")
    ax.grid(True, linestyle="--", alpha=0.4)
    ax.set_facecolor("#1e1e1e")
    ax.tick_params(colors='white')
    plt.tight_layout()
    return fig

def generar_grafica_dispersion():
    x = [i for i in range(20)]
    y = [random.randint(10, 50) for _ in range(20)]

    fig, ax = plt.subplots(figsize=(4, 3), facecolor="#1e1e1e")
    ax.scatter(x, y, color="#b197fc", alpha=0.8, edgecolors="white")
    ax.set_title("Muestreo de Sensores", fontsize=10, weight='bold', color="white")
    ax.set_facecolor("#1e1e1e")
    ax.tick_params(colors='white')
    plt.tight_layout()
    return fig

# --- GRÁFICA DE PASTEL ---
def generar_grafica_pastel():
    categorias = ["Comida", "Transporte", "Renta", "Entretenimiento"]
    gastos = [35, 20, 30, 15]

    fig, ax = plt.subplots(figsize=(4, 3), facecolor="#1e1e1e")
    ax.pie(
        gastos,
        labels=categorias,
        autopct='%1.1f%%',
        startangle=90,
        colors=["#4dabf7", "#ffa94d", "#51cf66", "#f783ac"],
        textprops={'color':"white"}
    )
    ax.set_title("Distribución de Gastos", fontsize=10, weight='bold', color="white")
    plt.tight_layout()
    return fig


def main(page: ft.Page):
    page.title = "Dashboard TAP"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#121212"
    page.vertical_alignment = "start"
    page.horizontal_alignment = "center"

    header = ft.Text(
        "Dashboard de Visualización de Datos",
        size=26,
        weight="bold",
        color="white"
    )

    tablero = ft.GridView(
        expand=True,
        runs_count=2,
        spacing=20,
        run_spacing=20,
        child_aspect_ratio=1.5,
    )

    # --- ESPACIO 1: BARRAS ---
    fig_1 = generar_grafica_barras()
    contenedor_1 = ft.Container(
        content=fch.MatplotlibChart(figure=fig_1),
        bgcolor="#1e1e1e",
        border_radius=12,
        padding=10,
        shadow=ft.BoxShadow(blur_radius=15, color="#00000066")
    )
    plt.close(fig_1)

    # --- ESPACIO 2: LÍNEAS ---
    fig_2 = generar_grafica_lineas()
    contenedor_2 = ft.Container(
        content=fch.MatplotlibChart(figure=fig_2),
        bgcolor="#1e1e1e",
        border_radius=12,
        padding=10,
        shadow=ft.BoxShadow(blur_radius=15, color="#00000066")
    )
    plt.close(fig_2)

    # --- ESPACIO 3: DISPERSIÓN ---
    fig_3 = generar_grafica_dispersion()
    contenedor_3 = ft.Container(
        content=fch.MatplotlibChart(figure=fig_3),
        bgcolor="#1e1e1e",
        border_radius=12,
        padding=10,
        shadow=ft.BoxShadow(blur_radius=15, color="#00000066")
    )
    plt.close(fig_3)

    # --- ESPACIO 4: PASTEL ---
    fig_4 = generar_grafica_pastel()
    contenedor_4 = ft.Container(
        content=fch.MatplotlibChart(figure=fig_4),
        bgcolor="#1e1e1e",
        border_radius=12,
        padding=10,
        shadow=ft.BoxShadow(blur_radius=15, color="#00000066")
    )
    plt.close(fig_4)

    tablero.controls.append(contenedor_1)
    tablero.controls.append(contenedor_2)
    tablero.controls.append(contenedor_3)
    tablero.controls.append(contenedor_4)

    page.add(header, ft.Divider(color="#333333"), tablero)


if __name__ == "__main__":
    ft.app(target=main)
```
<img width="1584" height="892" alt="image" src="https://github.com/user-attachments/assets/13c8e694-5ad0-4fbf-a388-0a3a59c76469" />

Este programa desarrolla una aplicación gráfica en Python que funciona como un dashboard de visualización de datos. Su objetivo principal es mostrar información de manera visual mediante diferentes tipos de gráficas dentro de una misma interfaz.

Para lograrlo, el código genera cuatro representaciones distintas de datos: una gráfica de barras para mostrar ventas por producto, una gráfica de líneas que representa una tendencia de rendimiento a lo largo del tiempo, una gráfica de dispersión que simula datos de sensores utilizando valores aleatorios, y una gráfica de pastel que ilustra la distribución de gastos en distintas categorías. Cada una de estas gráficas es creada de forma independiente y posteriormente integrada en la interfaz.

La aplicación utiliza un entorno visual que permite organizar estos elementos en una cuadrícula, lo que facilita ver todas las gráficas simultáneamente, como si se tratara de un panel de control o monitoreo. Además, se aplica un diseño en modo oscuro con estilos modernos, incluyendo contenedores con bordes redondeados y efectos visuales, lo que mejora la presentación.

En conjunto, el código demuestra cómo combinar librerías de visualización de datos con herramientas de interfaz gráfica para construir una aplicación completa que permite analizar información de forma clara, organizada y visualmente atractiva.

## 2.3 Creación de componentes (visuales y no visuales) definidos por el usuario

En el desarrollo de software, la creación de componentes definidos por el usuario es una práctica fundamental que permite estructurar las aplicaciones de manera modular, facilitando la reutilización del código, el mantenimiento y la escalabilidad. Un componente es una unidad independiente que encapsula funcionalidad específica y que puede integrarse dentro de un sistema más amplio.

Los componentes pueden clasificarse en dos grandes categorías: componentes visuales y componentes no visuales, dependiendo de si tienen o no representación gráfica dentro de la interfaz de usuario.

---

### Componentes visuales

Los componentes visuales son aquellos que forman parte de la interfaz gráfica de una aplicación y que interactúan directamente con el usuario. Estos componentes representan elementos visibles como botones, formularios, paneles, tarjetas, tablas, entre otros.

La creación de componentes visuales definidos por el usuario permite diseñar interfaces más organizadas y consistentes, ya que encapsulan tanto la estructura visual como el comportamiento asociado. Esto significa que un mismo componente puede reutilizarse múltiples veces en distintas partes de la aplicación sin necesidad de duplicar código.

Además, los componentes visuales suelen ser configurables mediante propiedades, lo que permite adaptar su comportamiento o apariencia según las necesidades específicas. Por ejemplo, un componente de tarjeta puede recibir datos diferentes para mostrar información personalizada sin modificar su estructura interna.

---

### Componentes no visuales

Por otro lado, los componentes no visuales son aquellos que no tienen representación gráfica, pero que cumplen funciones esenciales dentro del sistema. Estos componentes se encargan de la lógica del programa, como el procesamiento de datos, validaciones, acceso a bases de datos o comunicación con servicios externos.

A diferencia de los componentes visuales, estos se enfocan en la funcionalidad interna de la aplicación y suelen implementarse mediante funciones, clases o servicios. Su principal ventaja es que permiten separar la lógica del negocio de la interfaz de usuario, lo que mejora la organización del código y facilita su mantenimiento.

---

### Importancia de la creación de componentes

La creación de componentes definidos por el usuario es clave en el desarrollo moderno debido a que:

- Permite dividir sistemas complejos en partes más pequeñas y manejables.
- Facilita la reutilización del código en diferentes proyectos.
- Mejora la legibilidad y organización del software.
- Reduce la duplicación de código.
- Favorece el trabajo colaborativo en equipos de desarrollo.

---

### Buenas prácticas en la creación de componentes

Para lograr componentes eficientes y reutilizables, es importante seguir ciertas buenas prácticas:

- Diseñar componentes con una única responsabilidad.
- Mantener una estructura clara y bien organizada.
- Utilizar nombres descriptivos que reflejen su función.
- Evitar dependencias innecesarias entre componentes.
- Documentar su funcionamiento y forma de uso.

---

### Conclusión

La creación de componentes visuales y no visuales definidos por el usuario es una técnica esencial en la ingeniería de software. Permite desarrollar aplicaciones más estructuradas, reutilizables y fáciles de mantener. Al separar la lógica de la presentación y encapsular funcionalidades específicas, los desarrolladores pueden construir sistemas más robustos y adaptables a diferentes contextos y necesidades.

## 2.4 Creación y uso de paquetes/librerías definidas por el usuario

En el desarrollo de software, además de utilizar librerías proporcionadas por el lenguaje o por terceros, los desarrolladores tienen la posibilidad de crear sus propias librerías o paquetes con el objetivo de reutilizar código en distintos proyectos. Esta práctica es fundamental para mejorar la organización, eficiencia y mantenibilidad de las aplicaciones.

Una librería definida por el usuario es un conjunto de funciones, clases o componentes creados para resolver problemas específicos, mientras que un paquete es una estructura que agrupa estos elementos junto con otros recursos necesarios, como configuraciones y documentación.

---

### Proceso de creación de una librería o paquete

La creación de una librería o paquete implica una serie de pasos que permiten estructurar correctamente el código para su posterior reutilización:

En primer lugar, se debe identificar la funcionalidad que se desea encapsular. Esta funcionalidad debe ser lo suficientemente general como para poder utilizarse en diferentes contextos.

Posteriormente, se organiza el código en módulos o archivos, separando las distintas responsabilidades. Esta organización facilita la comprensión y el mantenimiento del sistema.

Una vez estructurado el código, es importante documentar su uso, especificando cómo se debe importar, qué parámetros recibe y qué resultados devuelve. La documentación es clave para que otros desarrolladores puedan utilizar la librería correctamente.

Finalmente, el paquete puede prepararse para su distribución, ya sea para uso interno en un proyecto o para su publicación en repositorios especializados.

---

### Uso de librerías definidas por el usuario

Una vez creada una librería o paquete, este puede ser reutilizado en diferentes partes de un mismo proyecto o incluso en otros proyectos. Para ello, generalmente se importa el módulo correspondiente y se utilizan sus funciones o clases según sea necesario.

El uso de librerías propias permite mantener el código más limpio, ya que evita la repetición de funciones y centraliza la lógica en un solo lugar.

---

### Ventajas de crear librerías propias

El desarrollo de librerías definidas por el usuario ofrece múltiples beneficios:

- Permite reutilizar código de manera eficiente.
- Mejora la organización del proyecto.
- Facilita el mantenimiento y actualización del software.
- Reduce la duplicación de código.
- Favorece el trabajo colaborativo al compartir funcionalidades comunes.

---

### Consideraciones importantes

Al crear paquetes o librerías propias, es importante tener en cuenta ciertos aspectos:

- Diseñar interfaces claras y fáciles de usar.
- Mantener una estructura organizada del código.
- Versionar adecuadamente la librería para controlar cambios.
- Documentar su funcionamiento de forma detallada.
- Asegurar la compatibilidad con el entorno donde será utilizada.

---

### Ejemplos de herramientas de gestión de paquetes

Existen diversas herramientas que permiten distribuir y gestionar paquetes en distintos lenguajes de programación, tales como gestores de paquetes. Estos facilitan la instalación, actualización y eliminación de librerías dentro de un proyecto.

---

### Conclusión

La creación y uso de paquetes y librerías definidas por el usuario es una práctica esencial en el desarrollo de software moderno. Permite construir aplicaciones más organizadas, reutilizables y escalables. Al encapsular funcionalidades específicas y facilitar su distribución, los desarrolladores pueden optimizar su trabajo y mejorar la calidad del software producido. 

## Proyecto Integrador
Este fue el proyecto integrador de la unidad 2, en el cual se desarrolla una aplicación gráfica completa que simula una tienda en línea de productos tecnológicos.

La aplicación muestra un catálogo de productos organizados en tarjetas visuales donde se presenta información como nombre, precio, descripción, categoría, imagen y disponibilidad. Cada producto permite al usuario interactuar mediante botones para agregarlo al carrito de compras o marcarlo como favorito.

El sistema incluye un carrito dinámico que almacena los productos seleccionados, permite aumentar o disminuir cantidades y calcula automáticamente el total de la compra. Además, se muestra un indicador visual con la cantidad de artículos agregados y un panel lateral donde se visualiza el resumen del carrito.

También se implementa un sistema de favoritos que permite al usuario guardar productos de interés, actualizando visualmente el estado de cada elemento. La interfaz utiliza un diseño moderno en modo oscuro, con estilos personalizados, tipografías y una organización responsiva.

En conjunto, el programa demuestra la creación y uso de componentes visuales, manejo de estado, interacción del usuario y reutilización de código, integrando los conceptos principales de componentes y librerías vistos en la unidad.

<img width="1584" height="892" alt="image" src="https://github.com/user-attachments/assets/fcab259a-3cf4-4565-a651-6f64393bc77f" />

## Conclusión de la unidad 2 

Componentes y Librerías permitió comprender la importancia de la modularidad y la reutilización en el desarrollo de software moderno. A lo largo de esta unidad se analizaron los conceptos fundamentales de componentes, librerías y paquetes, así como su aplicación práctica tanto con herramientas proporcionadas por el lenguaje como mediante la creación de soluciones propias.

Se aprendió que los componentes, ya sean visuales o no visuales, permiten estructurar mejor una aplicación al dividirla en partes independientes y reutilizables, facilitando su mantenimiento y escalabilidad. Asimismo, el uso de librerías estándar y externas contribuye a optimizar el tiempo de desarrollo y mejorar la calidad del código al aprovechar soluciones ya existentes y probadas.

Por otra parte, la creación de librerías y paquetes definidos por el usuario refuerza la capacidad de organizar proyectos de manera más profesional, promoviendo la reutilización del código y el trabajo colaborativo. Estos conocimientos se integraron en el desarrollo de un proyecto práctico, donde se aplicaron los conceptos vistos para construir una aplicación funcional.

En conclusión, esta unidad proporciona bases sólidas para el desarrollo de software estructurado, eficiente y escalable, destacando la importancia de utilizar y crear componentes y librerías como una práctica esencial en la programación actual.





