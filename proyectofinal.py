import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None


class ListaSimple:
    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):

        nuevo = Nodo(dato)

        if self.cabeza is None:
            self.cabeza = nuevo

        else:

            actual = self.cabeza

            while actual.siguiente:
                actual = actual.siguiente

            actual.siguiente = nuevo

    def obtener_lista(self):

        datos = []

        actual = self.cabeza

        while actual:
            datos.append(str(actual.dato))
            actual = actual.siguiente

        return datos


class ListaDoble:
    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):

        nuevo = Nodo(dato)

        if self.cabeza is None:
            self.cabeza = nuevo

        else:

            actual = self.cabeza

            while actual.siguiente:
                actual = actual.siguiente

            actual.siguiente = nuevo
            nuevo.anterior = actual

    def obtener_lista(self):

        datos = []

        actual = self.cabeza

        while actual:
            datos.append(actual.dato)
            actual = actual.siguiente

        return datos


class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, dato):
        self.items.append(dato)

    def obtener_lista(self):
        return list(reversed(self.items))


class Cola:
    def __init__(self):
        self.items = []

    def encolar(self, dato):
        self.items.append(dato)

    def desencolar(self):

        if len(self.items) > 0:
            return self.items.pop(0)

    def esta_vacia(self):
        return len(self.items) == 0

    def obtener_lista(self):
        return [str(item) for item in self.items]


class NodoArbol:
    def __init__(self, vuelo):

        self.vuelo = vuelo
        self.izquierda = None
        self.derecha = None


class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, vuelo):

        if self.raiz is None:
            self.raiz = NodoArbol(vuelo)

        else:
            self.insertar_recursivo(self.raiz, vuelo)

    def insertar_recursivo(self, nodo, vuelo):

        if vuelo.codigo < nodo.vuelo.codigo:

            if nodo.izquierda is None:
                nodo.izquierda = NodoArbol(vuelo)

            else:
                self.insertar_recursivo(
                    nodo.izquierda,
                    vuelo
                )

        else:

            if nodo.derecha is None:
                nodo.derecha = NodoArbol(vuelo)

            else:
                self.insertar_recursivo(
                    nodo.derecha,
                    vuelo
                )

    def buscar(self, codigo):

        return self.buscar_recursivo(
            self.raiz,
            codigo
        )

    def buscar_recursivo(self, nodo, codigo):

        if nodo is None:
            return None

        if nodo.vuelo.codigo == codigo:
            return nodo.vuelo

        if codigo < nodo.vuelo.codigo:

            return self.buscar_recursivo(
                nodo.izquierda,
                codigo
            )

        else:

            return self.buscar_recursivo(
                nodo.derecha,
                codigo
            )


class Persona:
    def __init__(self, nombre, identificacion):

        self.nombre = nombre
        self.identificacion = identificacion


class Pasajero(Persona):
    def __init__(self, nombre, identificacion, destino):

        super().__init__(
            nombre,
            identificacion
        )

        self.destino = destino

    def __str__(self):

        return (
            f"{self.nombre} | "
            f"ID: {self.identificacion} | "
            f"Destino: {self.destino}"
        )


class Piloto(Persona):
    def __init__(self, nombre, identificacion, experiencia):

        super().__init__(
            nombre,
            identificacion
        )

        self.experiencia = experiencia


class Tiquete:

    contador = 1

    def __init__(
        self,
        pasajero,
        vuelo,
        asiento,
        precio
    ):

        self.codigo = "TK" + str(Tiquete.contador)

        Tiquete.contador += 1

        self.pasajero = pasajero
        self.vuelo = vuelo
        self.asiento = asiento
        self.precio = precio

    def __str__(self):

        return (
            f"Tiquete: {self.codigo} | "
            f"Pasajero: {self.pasajero.nombre} | "
            f"Vuelo: {self.vuelo.codigo} | "
            f"Asiento: {self.asiento} | "
            f"Precio: ${self.precio}"
        )


class Vuelo:
    def __init__(
        self,
        codigo,
        destino,
        piloto,
        precio
    ):

        self.codigo = codigo
        self.destino = destino
        self.piloto = piloto
        self.precio = precio

        self.pasajeros = ListaSimple()

        self.tiquetes = ListaSimple()

        self.asientos_disponibles = [
            "A1", "A2", "A3",
            "B1", "B2", "B3",
            "C1", "C2", "C3"
        ]

    def agregar_pasajero(self, pasajero):

        self.pasajeros.agregar(pasajero)

    def vender_tiquete(self, pasajero):

        if len(self.asientos_disponibles) == 0:
            return "No hay asientos disponibles"

        asiento = self.asientos_disponibles.pop(0)

        tiquete = Tiquete(
            pasajero,
            self,
            asiento,
            self.precio
        )

        self.tiquetes.agregar(tiquete)
        self.pasajeros.agregar(pasajero)

        return str(tiquete)

    def __str__(self):

        return (
            f"Vuelo: {self.codigo} | "
            f"Destino: {self.destino} | "
            f"Precio: ${self.precio}"
        )


class Aeropuerto:
    def __init__(self, nombre):

        self.nombre = nombre

        self.lista_vuelos = ListaSimple()

        self.historial = ListaDoble()

        self.vuelos_despegados = Pila()

        self.cola_abordaje = Cola()

        self.arbol_vuelos = ArbolBinario()

    def registrar_vuelo(self, vuelo):

        self.lista_vuelos.agregar(vuelo)

        self.arbol_vuelos.insertar(vuelo)

        texto = f"Vuelo {vuelo.codigo} registrado"

        self.historial.agregar(texto)

    def vender_tiquete(self, codigo_vuelo, pasajero):

        vuelo = self.arbol_vuelos.buscar(
            codigo_vuelo
        )

        if vuelo is None:
            return "Vuelo no encontrado"

        resultado = vuelo.vender_tiquete(
            pasajero
        )

        texto = (
            f"Tiquete vendido a "
            f"{pasajero.nombre} "
            f"para el vuelo {codigo_vuelo}"
        )

        self.historial.agregar(texto)

        return resultado


aeropuerto = Aeropuerto(
    "Aeropuerto Internacional"
)


ventana = tk.Tk()

ventana.title(
    "Sistema de Gestión de Aeropuerto"
)

ventana.geometry("1500x850")

ventana.configure(bg="#1e1e2f")


titulo = tk.Label(
    ventana,
    text="✈ SISTEMA DE GESTIÓN DE AEROPUERTO ✈",
    font=("Arial", 24, "bold"),
    bg="#1e1e2f",
    fg="white"
)

titulo.pack(pady=15)


frame_principal = tk.Frame(
    ventana,
    bg="#1e1e2f"
)

frame_principal.pack(
    fill="both",
    expand=True
)


canvas_menu = tk.Canvas(
    frame_principal,
    bg="#252540",
    width=330,
    highlightthickness=0
)

scrollbar = tk.Scrollbar(
    frame_principal,
    orient="vertical",
    command=canvas_menu.yview
)

menu = tk.Frame(
    canvas_menu,
    bg="#252540"
)

menu.bind(
    "<Configure>",
    lambda e: canvas_menu.configure(
        scrollregion=canvas_menu.bbox("all")
    )
)

canvas_menu.create_window(
    (0, 0),
    window=menu,
    anchor="nw"
)

canvas_menu.configure(
    yscrollcommand=scrollbar.set
)

canvas_menu.pack(
    side="left",
    fill="y"
)

scrollbar.pack(
    side="left",
    fill="y"
)


contenido = tk.Frame(
    frame_principal,
    bg="#2f2f4f"
)

contenido.pack(
    side="right",
    fill="both",
    expand=True
)


area_texto = tk.Text(
    contenido,
    font=("Consolas", 12),
    bg="#151525",
    fg="white"
)

area_texto.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=20
)


def mostrar_texto(texto):

    area_texto.delete(
        "1.0",
        tk.END
    )

    area_texto.insert(
        tk.END,
        texto
    )


def registrar_vuelo():

    ventana_registro = tk.Toplevel()

    ventana_registro.title(
        "Registrar Vuelo"
    )

    ventana_registro.geometry(
        "400x450"
    )

    tk.Label(
        ventana_registro,
        text="Código"
    ).pack()

    codigo = tk.Entry(
        ventana_registro
    )

    codigo.pack()

    tk.Label(
        ventana_registro,
        text="Destino"
    ).pack()

    destino = tk.Entry(
        ventana_registro
    )

    destino.pack()

    tk.Label(
        ventana_registro,
        text="Precio"
    ).pack()

    precio = tk.Entry(
        ventana_registro
    )

    precio.pack()

    tk.Label(
        ventana_registro,
        text="Piloto"
    ).pack()

    piloto_nombre = tk.Entry(
        ventana_registro
    )

    piloto_nombre.pack()

    tk.Label(
        ventana_registro,
        text="ID Piloto"
    ).pack()

    piloto_id = tk.Entry(
        ventana_registro
    )

    piloto_id.pack()

    tk.Label(
        ventana_registro,
        text="Experiencia"
    ).pack()

    experiencia = tk.Entry(
        ventana_registro
    )

    experiencia.pack()

    def guardar():

        piloto = Piloto(
            piloto_nombre.get(),
            piloto_id.get(),
            experiencia.get()
        )

        vuelo = Vuelo(
            codigo.get(),
            destino.get(),
            piloto,
            float(precio.get())
        )

        aeropuerto.registrar_vuelo(
            vuelo
        )

        messagebox.showinfo(
            "Éxito",
            "Vuelo registrado correctamente"
        )

        ventana_registro.destroy()

    tk.Button(
        ventana_registro,
        text="Guardar Vuelo",
        bg="#3b82f6",
        fg="white",
        command=guardar
    ).pack(pady=20)


def vender_tiquete():

    ventana_tiquete = tk.Toplevel()

    ventana_tiquete.title(
        "Venta de Tiquete"
    )

    ventana_tiquete.geometry(
        "400x400"
    )

    tk.Label(
        ventana_tiquete,
        text="Código vuelo"
    ).pack()

    codigo = tk.Entry(
        ventana_tiquete
    )

    codigo.pack()

    tk.Label(
        ventana_tiquete,
        text="Nombre pasajero"
    ).pack()

    nombre = tk.Entry(
        ventana_tiquete
    )

    nombre.pack()

    tk.Label(
        ventana_tiquete,
        text="Identificación"
    ).pack()

    identificacion = tk.Entry(
        ventana_tiquete
    )

    identificacion.pack()

    tk.Label(
        ventana_tiquete,
        text="Destino"
    ).pack()

    destino = tk.Entry(
        ventana_tiquete
    )

    destino.pack()

    def vender():

        pasajero = Pasajero(
            nombre.get(),
            identificacion.get(),
            destino.get()
        )

        resultado = aeropuerto.vender_tiquete(
            codigo.get(),
            pasajero
        )

        messagebox.showinfo(
            "Tiquete",
            resultado
        )

        ventana_tiquete.destroy()

    tk.Button(
        ventana_tiquete,
        text="Vender",
        bg="#10b981",
        fg="white",
        command=vender
    ).pack(pady=20)


def agregar_cola():

    ventana_cola = tk.Toplevel()

    ventana_cola.title(
        "Agregar Pasajero a Cola"
    )

    ventana_cola.geometry(
        "400x350"
    )

    tk.Label(
        ventana_cola,
        text="Nombre"
    ).pack()

    nombre = tk.Entry(
        ventana_cola
    )

    nombre.pack()

    tk.Label(
        ventana_cola,
        text="Identificación"
    ).pack()

    identificacion = tk.Entry(
        ventana_cola
    )

    identificacion.pack()

    tk.Label(
        ventana_cola,
        text="Destino"
    ).pack()

    destino = tk.Entry(
        ventana_cola
    )

    destino.pack()

    def guardar():

        pasajero = Pasajero(
            nombre.get(),
            identificacion.get(),
            destino.get()
        )

        aeropuerto.cola_abordaje.encolar(
            pasajero
        )

        aeropuerto.historial.agregar(
            f"Pasajero {nombre.get()} agregado a cola"
        )

        messagebox.showinfo(
            "Éxito",
            "Pasajero agregado a la cola"
        )

        ventana_cola.destroy()

    tk.Button(
        ventana_cola,
        text="Agregar",
        bg="#06b6d4",
        fg="white",
        command=guardar
    ).pack(pady=20)


def abordar_pasajero():

    ventana_abordar = tk.Toplevel()

    ventana_abordar.title(
        "Abordar Pasajero"
    )

    ventana_abordar.geometry(
        "350x200"
    )

    tk.Label(
        ventana_abordar,
        text="Código del vuelo"
    ).pack()

    codigo = tk.Entry(
        ventana_abordar
    )

    codigo.pack()

    def abordar():

        vuelo = aeropuerto.arbol_vuelos.buscar(
            codigo.get()
        )

        if vuelo is None:

            messagebox.showerror(
                "Error",
                "Vuelo no encontrado"
            )

            return

        if aeropuerto.cola_abordaje.esta_vacia():

            messagebox.showerror(
                "Error",
                "No hay pasajeros en cola"
            )

            return

        pasajero = aeropuerto.cola_abordaje.desencolar()

        vuelo.agregar_pasajero(
            pasajero
        )

        aeropuerto.historial.agregar(
            f"{pasajero.nombre} abordó vuelo {codigo.get()}"
        )

        messagebox.showinfo(
            "Éxito",
            "Pasajero abordó correctamente"
        )

        ventana_abordar.destroy()

    tk.Button(
        ventana_abordar,
        text="Abordar",
        bg="#8b5cf6",
        fg="white",
        command=abordar
    ).pack(pady=20)


def despegar_vuelo():

    ventana_despegue = tk.Toplevel()

    ventana_despegue.title(
        "Despegar Vuelo"
    )

    ventana_despegue.geometry(
        "350x200"
    )

    tk.Label(
        ventana_despegue,
        text="Código del vuelo"
    ).pack()

    codigo = tk.Entry(
        ventana_despegue
    )

    codigo.pack()

    def despegar():

        vuelo = aeropuerto.arbol_vuelos.buscar(
            codigo.get()
        )

        if vuelo is None:

            messagebox.showerror(
                "Error",
                "Vuelo no encontrado"
            )

            return

        aeropuerto.vuelos_despegados.apilar(
            vuelo.codigo
        )

        aeropuerto.historial.agregar(
            f"Vuelo {vuelo.codigo} despegó"
        )

        messagebox.showinfo(
            "Éxito",
            "Vuelo despegó correctamente"
        )

        ventana_despegue.destroy()

    tk.Button(
        ventana_despegue,
        text="Despegar",
        bg="#ec4899",
        fg="white",
        command=despegar
    ).pack(pady=20)


def mostrar_vuelos():

    vuelos = aeropuerto.lista_vuelos.obtener_lista()

    texto = "\n\n".join(vuelos)

    mostrar_texto(texto)


def mostrar_cola():

    datos = aeropuerto.cola_abordaje.obtener_lista()

    texto = "\n\n".join(datos)

    mostrar_texto(texto)


def mostrar_historial():

    historial = aeropuerto.historial.obtener_lista()

    texto = "\n\n".join(historial)

    mostrar_texto(texto)


def mostrar_historial_inverso():

    datos = aeropuerto.historial.obtener_lista()

    datos.reverse()

    texto = "\n\n".join(datos)

    mostrar_texto(texto)


def mostrar_pila():

    datos = aeropuerto.vuelos_despegados.obtener_lista()

    texto = "\n\n".join(datos)

    mostrar_texto(texto)


def buscar_vuelo():

    ventana_buscar = tk.Toplevel()

    ventana_buscar.title(
        "Buscar Vuelo"
    )

    ventana_buscar.geometry(
        "350x200"
    )

    tk.Label(
        ventana_buscar,
        text="Código del vuelo"
    ).pack()

    codigo = tk.Entry(
        ventana_buscar
    )

    codigo.pack()

    def buscar():

        vuelo = aeropuerto.arbol_vuelos.buscar(
            codigo.get()
        )

        if vuelo:

            mostrar_texto(str(vuelo))

        else:

            messagebox.showerror(
                "Error",
                "Vuelo no encontrado"
            )

    tk.Button(
        ventana_buscar,
        text="Buscar",
        bg="#0ea5e9",
        fg="white",
        command=buscar
    ).pack(pady=20)


def mostrar_asientos():

    ventana_asientos = tk.Toplevel()

    ventana_asientos.title(
        "Mostrar Asientos"
    )

    ventana_asientos.geometry(
        "350x250"
    )

    tk.Label(
        ventana_asientos,
        text="Código del vuelo"
    ).pack()

    codigo = tk.Entry(
        ventana_asientos
    )

    codigo.pack()

    def mostrar():

        vuelo = aeropuerto.arbol_vuelos.buscar(
            codigo.get()
        )

        if vuelo:

            texto = "\n".join(
                vuelo.asientos_disponibles
            )

            mostrar_texto(texto)

        else:

            messagebox.showerror(
                "Error",
                "Vuelo no encontrado"
            )

    tk.Button(
        ventana_asientos,
        text="Mostrar",
        bg="#6366f1",
        fg="white",
        command=mostrar
    ).pack(pady=20)


def mostrar_arbol():

    vuelos = aeropuerto.lista_vuelos.obtener_lista()

    texto = "ÁRBOL DE VUELOS\n\n"

    for vuelo in vuelos:
        texto += vuelo + "\n\n"

    mostrar_texto(texto)


def guardar_historial():

    archivo = open(
        "historial_aeropuerto.txt",
        "w",
        encoding="utf-8"
    )

    historial = aeropuerto.historial.obtener_lista()

    for dato in historial:
        archivo.write(dato + "\n")

    archivo.close()

    messagebox.showinfo(
        "Éxito",
        "Historial guardado correctamente"
    )


def mostrar_pasajeros_vuelo():

    ventana_pasajeros = tk.Toplevel()

    ventana_pasajeros.title(
        "Pasajeros del Vuelo"
    )

    ventana_pasajeros.geometry(
        "350x200"
    )

    tk.Label(
        ventana_pasajeros,
        text="Código del vuelo"
    ).pack()

    codigo = tk.Entry(
        ventana_pasajeros
    )

    codigo.pack()

    def mostrar():

        vuelo = aeropuerto.arbol_vuelos.buscar(
            codigo.get()
        )

        if vuelo:

            datos = vuelo.pasajeros.obtener_lista()

            texto = "\n\n".join(datos)

            mostrar_texto(texto)

        else:

            messagebox.showerror(
                "Error",
                "Vuelo no encontrado"
            )

    tk.Button(
        ventana_pasajeros,
        text="Mostrar",
        bg="#eab308",
        fg="white",
        command=mostrar
    ).pack(pady=20)


def mostrar_tiquetes():

    ventana_tiquetes = tk.Toplevel()

    ventana_tiquetes.title(
        "Mostrar Tiquetes"
    )

    ventana_tiquetes.geometry(
        "350x200"
    )

    tk.Label(
        ventana_tiquetes,
        text="Código del vuelo"
    ).pack()

    codigo = tk.Entry(
        ventana_tiquetes
    )

    codigo.pack()

    def mostrar():

        vuelo = aeropuerto.arbol_vuelos.buscar(
            codigo.get()
        )

        if vuelo:

            datos = vuelo.tiquetes.obtener_lista()

            texto = "\n\n".join(datos)

            mostrar_texto(texto)

        else:

            messagebox.showerror(
                "Error",
                "Vuelo no encontrado"
            )

    tk.Button(
        ventana_tiquetes,
        text="Mostrar",
        bg="#f43f5e",
        fg="white",
        command=mostrar
    ).pack(pady=20)


botones = [

    ("Registrar Vuelo", "#3b82f6", registrar_vuelo),
    ("Vender Tiquete", "#10b981", vender_tiquete),
    ("Agregar a Cola", "#06b6d4", agregar_cola),
    ("Abordar Pasajero", "#8b5cf6", abordar_pasajero),
    ("Despegar Vuelo", "#ec4899", despegar_vuelo),
    ("Mostrar Vuelos", "#6366f1", mostrar_vuelos),
    ("Mostrar Cola", "#14b8a6", mostrar_cola),
    ("Mostrar Historial", "#f59e0b", mostrar_historial),
    ("Historial Inverso", "#f97316", mostrar_historial_inverso),
    ("Vuelos Despegados", "#84cc16", mostrar_pila),
    ("Buscar Vuelo", "#0ea5e9", buscar_vuelo),
    ("Mostrar Árbol", "#a855f7", mostrar_arbol),
    ("Guardar Historial", "#22c55e", guardar_historial),
    ("Pasajeros Vuelo", "#eab308", mostrar_pasajeros_vuelo),
    ("Mostrar Tiquetes", "#f43f5e", mostrar_tiquetes),
    ("Mostrar Asientos", "#6366f1", mostrar_asientos),
    ("Salir", "#ef4444", ventana.destroy)

]


for texto, color, funcion in botones:

    boton = tk.Button(
        menu,
        text=texto,
        font=("Arial", 12, "bold"),
        bg=color,
        fg="white",
        width=24,
        height=2,
        command=funcion
    )

    boton.pack(pady=10)


ventana.mainloop()


for texto, color, funcion in botones:

    boton = tk.Button(
        menu,
        text=texto,
        font=("Arial", 12, "bold"),
        bg=color,
        fg="white",
        width=24,
        height=2,
        command=funcion
    )

    boton.pack(pady=10)


ventana.mainloop()