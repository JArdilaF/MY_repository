import tkinter as tk
from tkinter import messagebox, simpledialog
import networkx as nx
import matplotlib.pyplot as plt


class Tanque:
    def __init__(self, nombre, capacidad):
        self.nombre = nombre
        self.capacidad = capacidad
        self.actual = 0
        self.lleno = False


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
        conexiones = [
            (dest, dist) for dest, dist in self.conexiones[tanque_actual].items()
            if not self.tanques[dest].lleno and dest not in visitados
        ]
        conexiones.sort(key=lambda x: x[1])
        return conexiones[0][0] if conexiones else None


class Interfaz:
    def __init__(self, root, grafo):
        self.root = root
        self.grafo = grafo
        self.root.title("Gestión de Tanques de Agua")
        self.root.geometry("1200x700")
        self.root.config(bg="lightgray")
        self.procesando = False
        self.barras = {}

        self.crear_botones_opciones()
        self.tanque_frame = tk.Frame(root, bg="lightgray")
        self.tanque_frame.pack(pady=20)

        self.info = tk.Text(root, height=10, width=100, bg="white", fg="black", font=("Arial", 10))
        self.info.pack(pady=10)

    def crear_botones_opciones(self):
        opciones_frame = tk.Frame(self.root, bg="lightgray")
        opciones_frame.pack(pady=10)

        btn_agregar_tanque = tk.Button(opciones_frame, text="Agregar Tanque", command=self.agregar_tanque,
                                       bg="blue", fg="white", font=("Arial", 12), width=20)
        btn_agregar_tanque.grid(row=0, column=0, padx=10, pady=10)

        btn_agregar_conexion = tk.Button(opciones_frame, text="Agregar Conexión", command=self.agregar_conexion,
                                         bg="green", fg="white", font=("Arial", 12), width=20)
        btn_agregar_conexion.grid(row=0, column=1, padx=10, pady=10)

        btn_visualizar_grafo = tk.Button(opciones_frame, text="Visualizar Grafo", command=self.visualizar_grafo,
                                         bg="purple", fg="white", font=("Arial", 12), width=20)
        btn_visualizar_grafo.grid(row=0, column=2, padx=10, pady=10)

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

    def vaciar_tanque(self, tanque_nombre):
        tanque = self.grafo.tanques[tanque_nombre]
        tanque.actual = 0
        tanque.lleno = False
        self.actualizar_barras(tanque_nombre, tanque.actual, tanque.capacidad)
        self.actualizar_info()
        messagebox.showinfo("Tanque Vaciado", f"El tanque {tanque_nombre} ha sido vaciado.")

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
            tk.Label(self.tanque_frame, text=nombre, font=("Arial", 14), bg="lightgray").grid(row=0, column=idx, padx=20)
            canvas = tk.Canvas(self.tanque_frame, width=100, height=200, bg="white", highlightthickness=1, relief="solid")
            canvas.grid(row=1, column=idx, padx=20)
            tk.Button(self.tanque_frame, text=f"Lluvia en {nombre}",
                      command=lambda t=nombre: self.iniciar_lluvia(t)).grid(row=2, column=idx, pady=10)
            tk.Button(self.tanque_frame, text=f"Vaciar {nombre}",
                      command=lambda t=nombre: self.vaciar_tanque(t)).grid(row=3, column=idx, pady=10)
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


# Configuración inicial
grafo = GrafoTanques()

# Crear la aplicación
root = tk.Tk()
app = Interfaz(root, grafo)
root.mainloop()
