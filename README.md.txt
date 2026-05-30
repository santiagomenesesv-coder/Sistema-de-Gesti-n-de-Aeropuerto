# Sistema de Gestión de Aeropuerto

## Descripción

Este proyecto consiste en un Sistema de Gestión de Aeropuerto desarrollado en Python utilizando Programación Orientada a Objetos (POO) e implementando diferentes estructuras de datos vistas durante el curso.

El sistema permite registrar vuelos, vender tiquetes, gestionar pasajeros, controlar abordajes, almacenar historial de operaciones y administrar vuelos despegados mediante una interfaz gráfica desarrollada con Tkinter.

## Autor

Santiago Meneses Vanegas

## Objetivo del Proyecto

Desarrollar una aplicación que simule el funcionamiento básico de un aeropuerto aplicando:

- Programación Orientada a Objetos.
- Herencia.
- Encapsulamiento.
- Listas simples.
- Listas dobles.
- Pilas.
- Colas.
- Árboles binarios.
- Interfaces gráficas con Tkinter.

## Estructuras de Datos Utilizadas

### Lista Simple

Utilizada para almacenar:

- Vuelos registrados.
- Pasajeros de cada vuelo.
- Tiquetes vendidos.

### Lista Doble

Utilizada para almacenar:

- Historial de acciones realizadas en el sistema.

### Cola

Utilizada para administrar:

- Cola de abordaje de pasajeros.

### Pila

Utilizada para almacenar:

- Vuelos que ya despegaron.

### Árbol Binario de Búsqueda

Utilizado para:

- Buscar vuelos por código de manera eficiente.

## Clases Implementadas

### Persona

Clase base del sistema.

### Pasajero

Hereda de Persona.

### Piloto

Hereda de Persona.

### Tiquete

Representa un tiquete de vuelo.

### Vuelo

Contiene información de:

- Código.
- Destino.
- Piloto.
- Precio.
- Pasajeros.
- Tiquetes.
- Asientos disponibles.

### Aeropuerto

Clase principal encargada de administrar todo el sistema.

## Funcionalidades

El sistema permite:

### Gestión de vuelos

- Registrar vuelos.
- Buscar vuelos.
- Mostrar vuelos.
- Mostrar árbol de vuelos.

### Gestión de pasajeros

- Agregar pasajeros a la cola.
- Abordar pasajeros.
- Mostrar pasajeros de un vuelo.

### Gestión de tiquetes

- Vender tiquetes.
- Mostrar tiquetes vendidos.

### Gestión de asientos

- Mostrar asientos disponibles.

### Gestión de historial

- Mostrar historial.
- Mostrar historial inverso.
- Guardar historial en archivo de texto.

### Gestión de despegues

- Despegar vuelos.
- Mostrar vuelos despegados.

## Interfaz Gráfica

La interfaz fue desarrollada con Tkinter e incluye:

- Menú lateral con desplazamiento vertical.
- Botones interactivos.
- Ventanas emergentes para ingreso de datos.
- Área central de visualización de información.
- Diseño moderno con colores personalizados.

## Cómo Ejecutar el Proyecto

### 1. Clonar el repositorio

```bash
git clone https://github.com/tuusuario/sistema-aeropuerto.git
```

### 2. Entrar a la carpeta

```bash
cd sistema-aeropuerto
```

### 3. Ejecutar el programa

```bash
python proyecto.py
```

## Archivos del Proyecto

```text
sistema-aeropuerto/
│
├── proyecto.py
├── historial_aeropuerto.txt
├── README.md
└── capturas/
```

## Tecnologías Utilizadas

- Python 3
- Tkinter

## Conceptos Aplicados

- Programación Orientada a Objetos.
- Herencia.
- Polimorfismo.
- Listas Enlazadas.
- Listas Doblemente Enlazadas.
- Pilas.
- Colas.
- Árboles Binarios de Búsqueda.
- Interfaces Gráficas.

## Mejoras Futuras

- Persistencia de datos con bases de datos.
- Generación de reportes en PDF.
- Validación avanzada de datos.
- Sistema de usuarios y autenticación.
- Gestión de múltiples aeropuertos.
- Estadísticas de vuelos.
- Panel administrativo.
- Exportación de información a Excel.

## Proyecto Académico

Proyecto desarrollado como trabajo final de la asignatura de Programación Orientada a Objetos, aplicando estructuras de datos y conceptos fundamentales de programación en Python.