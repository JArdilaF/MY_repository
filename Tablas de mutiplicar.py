import tkinter as tk
from tkinter import messagebox, simpledialog
import networkx as nx
import matplotlib.pyplot as plt


class Tanque:
    def __init__(self, nombre, capacidad):
        self.nombre = nombre
        self.capacidad = capacidad
        self.actual = 0  # Nivel actual de agua
        self.lleno = False  # Indica si el tanque está completamente lleno


class GrafoTanques:
    def __init__(self):
        self.tanques = {}
        self.conexiones = {}
        self.grafo_nx = nx.Graph()

    def agregar_tanque(self, nombre, capacidad):
        self.tanques[nombre] = Tanque(nombre, capacidad)
        self.conexiones[nombre] = {}
        self.grafo_nx.add_node(nombre)

    def agregar_conexion(self, origen, destino, distancia):
        if origen in self.conexiones and destino in self.conexiones:
            self.conexiones[origen][destino] = distancia
            self.conexiones[destino][origen] = distancia
            self.grafo_nx.add_edge(origen, destino, weight=distancia)

    def obtener_siguiente_tanque(self, tanque_actual, visitados):
        """Obtiene el tanque más cercano que aún no esté lleno ni visitado."""
        conexiones = [
            (dest, dist) for dest, dist in self.conexiones[tanque_actual].items()
            if not self.tanques[dest].lleno and dest not in visitados
        ]
        conexiones.sort(key=lambda x: x[1])  # Ordenar por distancia
        return conexiones[0][0] if conexiones else None


class Interfaz:
    def __init__(self, root, grafo):
        self.root = root
        self.grafo = grafo
        self.root.title("Gestión de Tanques de Agua")
        self.root.geometry("1000x600")
        self.procesando = False
        self.barras = {}

        self.root.config(bg="#f0f8ff")  # Fondo azul claro

        # Título principal
        tk.Label(self.root, text="Gestión de Tanques de Agua", font=("Arial", 24, "bold"), bg="#f0f8ff", fg="darkblue").pack(pady=20)

        # Botones principales
        self.crear_botones()

        # Frame para los tanques
        self.tanque_frame = tk.Frame(self.root, bg="#f0f8ff")
        self.tanque_frame.pack(pady=20)

        # Área de información
        self.info = tk.Text(self.root, height=10, width=80)
        self.info.pack(pady=10)

    def crear_botones(self):
        # Botones para las opciones
        opciones_frame = tk.Frame(self.root, bg="#f0f8ff")
        opciones_frame.pack(pady=10)

        # Botón Agregar Tanque
        boton_agregar_tanque = tk.Button(opciones_frame, text="Agregar Tanque", font=("Arial", 14), bg="lightblue", fg="darkblue", width=20, height=2, relief="solid", command=self.agregar_tanque)
        boton_agregar_tanque.grid(row=0, column=0, padx=10, pady=10)

        # Botón Agregar Conexión
        boton_agregar_conexion = tk.Button(opciones_frame, text="Agregar Conexión", font=("Arial", 14), bg="lightblue", fg="darkblue", width=20, height=2, relief="solid", command=self.agregar_conexion)
        boton_agregar_conexion.grid(row=0, column=1, padx=10, pady=10)

        # Botón Visualizar Grafo
        boton_visualizar_grafo = tk.Button(opciones_frame, text="Visualizar Grafo", font=("Arial", 14), bg="lightblue", fg="darkblue", width=20, height=2, relief="solid", command=self.visualizar_grafo)
        boton_visualizar_grafo.grid(row=0, column=2, padx=10, pady=10)

        # Botón Vaciar Tanques
        boton_vaciar_tanques = tk.Button(opciones_frame, text="Vaciar Tanques", font=("Arial", 14), bg="lightblue", fg="darkblue", width=20, height=2, relief="solid", command=self.vaciar_tanques)
        boton_vaciar_tanques.grid(row=0, column=3, padx=10, pady=10)

    def agregar_tanque(self):
        nombre = simpledialog.askstring("Agregar Tanque", "Nombre del tanque:")
        if not nombre:
            return
        capacidad = simpledialog.askinteger("Capacidad", f"Capacidad de {nombre} (en litros):", minvalue=1)
        if capacidad:
            self.grafo.agregar_tanque(nombre, capacidad)
            self.actualizar_visual()

    def agregar_conexion(self):
        origen = simpledialog.askstring("Conexión", "Tanque de origen:")
        destino = simpledialog.askstring("Conexión", "Tanque de destino:")
        if origen in self.grafo.tanques and destino in self.grafo.tanques:
            distancia = simpledialog.askinteger("Distancia", f"Distancia entre {origen} y {destino} (en km):", minvalue=1)
            if distancia:
                self.grafo.agregar_conexion(origen, destino, distancia)
        else:
            messagebox.showerror("Error", "Tanques no encontrados.")

    def iniciar_lluvia(self, tanque_inicial):
        if self.procesando:
            messagebox.showwarning("Simulación en curso", "Ya hay una simulación en progreso. Por favor, espere.")
            return
        self.procesando = True
        self.simular_llenado(tanque_inicial)

    def simular_llenado(self, tanque_inicial):
        visitados = set()
        actual = tanque_inicial

        while True:
            self.llenar_tanque(actual)
            visitados.add(actual)

            siguiente = self.grafo.obtener_siguiente_tanque(actual, visitados)
            if siguiente:
                actual = siguiente
            else:
                if all(tan.lleno for tan in self.grafo.tanques.values()):
                    messagebox.showinfo("Completado", "Todos los tanques están llenos.")
                    self.procesando = False
                    break

    def llenar_tanque(self, tanque_nombre):
        tanque = self.grafo.tanques[tanque_nombre]
        while tanque.actual < tanque.capacidad:
            tanque.actual += 10
            if tanque.actual >= tanque.capacidad:
                tanque.actual = tanque.capacidad
                tanque.lleno = True
            self.actualizar_barras(tanque_nombre, tanque.actual, tanque.capacidad)
            self.actualizar_info()
            self.root.update()
            self.root.after(100)

    def vaciar_tanques(self):
        """Vacía todos los tanques y los reinicia."""
        for nombre, tanque in self.grafo.tanques.items():
            tanque.actual = 0
            tanque.lleno = False
            self.actualizar_barras(nombre, tanque.actual, tanque.capacidad)
        self.actualizar_info()
        messagebox.showinfo("Tanques vaciados", "Todos los tanques han sido vaciados y están listos para llenarse nuevamente.")

    def visualizar_grafo(self):
        if not self.grafo.grafo_nx.nodes:
            messagebox.showerror("Error", "El grafo está vacío.")
            return
        pos = nx.spring_layout(self.grafo.grafo_nx)
        nx.draw(self.grafo.grafo_nx, pos, with_labels=True, node_size=3000, node_color="lightblue", font_size=10)
        labels = nx.get_edge_attributes(self.grafo.grafo_nx, "weight")
        nx.draw_networkx_edge_labels(self.grafo.grafo_nx, pos, edge_labels=labels)
        plt.title("Visualización del Grafo de Tanques")
        plt.show()

    def actualizar_visual(self):
        for widget in self.tanque_frame.winfo_children():
            widget.destroy()

        for idx, (nombre, tanque) in enumerate(self.grafo.tanques.items()):
            tk.Label(self.tanque_frame, text=nombre, font=("Arial", 14)).grid(row=0, column=idx, padx=20)
            canvas = tk.Canvas(self.tanque_frame, width=100, height=200, bg="white", highlightthickness=1, relief="solid")
            canvas.grid(row=1, column=idx, padx=20)
            tk.Button(self.tanque_frame, text=f"Lluvia en {nombre}",
                      command=lambda t=nombre: self.iniciar_lluvia(t), bg="lightblue", fg="darkblue", relief="raised", width=20, height=2).grid(row=2, column=idx, pady=10)
            self.barras[nombre] = canvas

    def actualizar_barras(self, nombre, nivel_actual, capacidad):
        canvas = self.barras[nombre]
        canvas.delete("all")
        altura = int((nivel_actual / capacidad) * 200)
        canvas.create_rectangle(10, 200 - altura, 90, 200, fill="blue", outline="black")

    def actualizar_info(self):
        self.info.delete(1.0, tk.END)
        for nombre, tanque in self.grafo.tanques.items():
            porcentaje = (tanque.actual / tanque.capacidad) * 100
            self.info.insert(tk.END, f"Tanque {nombre}: {tanque.actual}/{tanque.capacidad} litros ({porcentaje:.1f}%)\n")


class InterfazInicial:
    def __init__(self, root):
        self.root = root
        self.root.title("Pantalla Inicial")
        self.root.geometry("600x400")
        self.root.config(bg="#e0f7fa")  # Fondo verde claro

        tk.Label(self.root, text="CADA GOTA CUENTA", font=("Impact", 28, "bold"), fg="darkblue", bg="#e0f7fa").pack(pady=50)

        # Botón estilizado para iniciar la aplicación
        iniciar_btn = tk.Button(
            self.root,
            text="INICIAR PROGRAMA",
            font=("Arial", 16, "bold"),
            bg="lightblue",
            fg="darkblue",
            relief="raised",
            borderwidth=3,
            padx=20,
            pady=10,
            command=self.iniciar_aplicacion
        )
        iniciar_btn.pack(pady=20)

    def iniciar_aplicacion(self):
        self.root.destroy()
        root_principal = tk.Tk()
        grafo = GrafoTanques()
        Interfaz(root_principal, grafo)
        root_principal.mainloop()


# Iniciar aplicación
root_inicial = tk.Tk()
app_inicial = InterfazInicial(root_inicial)
root_inicial.mainloop()