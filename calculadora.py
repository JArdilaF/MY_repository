from tkinter import *
from tkinter import messagebox

ventana_calcular = Tk()
ventana_calcular.title("Calculadora")
ventana_calcular.geometry("300x400+468+132")#Tamaño y posicinamiento de la ventana
ventana_calcular.resizable(0, 0) #No permite redimensionar la ventana
ventana_calcular.configure(bg="#1E3A5F") #Color de fondo sexagesimal

frame_teclas = Frame(ventana_calcular, width=250, height=300)
frame_teclas.place(relx=0.5, rely=0.6, anchor="center")
frame_teclas.configure(bg="#4682B4")

lista_teclas = []

def agregar_1():
    lista_teclas.append("1")
    etiqueta_expresion.config(text=lista_teclas)

def agregar_2():
    lista_teclas.append("2")
    etiqueta_expresion.config(text=lista_teclas)

def agregar_3():
    lista_teclas.append("3")
    etiqueta_expresion.config(text=lista_teclas)

def agregar_4():
    lista_teclas.append("4")
    etiqueta_expresion.config(text=lista_teclas)

def agregar_5():
    lista_teclas.append("5")
    etiqueta_expresion.config(text=lista_teclas)

def agregar_6():
    lista_teclas.append("6")
    etiqueta_expresion.config(text=lista_teclas)

def agregar_7():
    lista_teclas.append("7")
    etiqueta_expresion.config(text=lista_teclas)

def agregar_8():
    lista_teclas.append("8")
    etiqueta_expresion.config(text=lista_teclas)

def agregar_9():
    lista_teclas.append("9")
    etiqueta_expresion.config(text=lista_teclas)

def agregar_0():
    lista_teclas.append("0")
    etiqueta_expresion.config(text=lista_teclas)

def agregar_suma():
    if resultado is not None:
        lista_teclas.clear()
        lista_teclas.append(str(resultado))

    if not lista_teclas:
        return

    if lista_teclas[-1] in ["+", "-", "*", "/"]:
        messagebox.showerror("Advertencia", "No se pueden agregar dos operadores seguidos")
        return

    lista_teclas.append("+")
    etiqueta_expresion.config(text=lista_teclas)

def agregar_resta():
    if resultado is not None:
        lista_teclas.clear()
        lista_teclas.append(str(resultado))

    if not lista_teclas:
        return
    
    if lista_teclas[-1] in ["+", "-", "*", "/"]:
        messagebox.showerror("Advertencia", "No se pueden agregar dos operadores seguidos")
        return
    
    lista_teclas.append("-")
    etiqueta_expresion.config(text=lista_teclas)

def agregar_multiplicacion():
    if resultado is not None:
        lista_teclas.clear()
        lista_teclas.append(str(resultado))

    if not lista_teclas:
        return
    
    if lista_teclas[-1] in ["+", "-", "*", "/"]:
        messagebox.showerror("Advertencia", "No se pueden agregar dos operadores seguidos")
        return

    lista_teclas.append("*")
    etiqueta_expresion.config(text=lista_teclas)

def agregar_division():
    if resultado is not None:
        lista_teclas.clear()
        lista_teclas.append(str(resultado))

    if not lista_teclas:
        return
    
    if lista_teclas[-1] in ["+", "-", "*", "/"]:
        messagebox.showerror("Advertencia", "No se pueden agregar dos operadores seguidos")
        return
    
    lista_teclas.append("/")
    etiqueta_expresion.config(text=lista_teclas)

def borrar(lista_teclas):
    if not lista_teclas:
        return

    lista_teclas.clear()  
    etiqueta_expresion.config(text=lista_teclas)
    
    etiqueta_resultado.config(text=lista_teclas)

resultado = None  

def calcular(lista_teclas):
    global resultado

    if not lista_teclas:
        messagebox.showerror("Error", "No hay nada que calcular")
        return
    
    if lista_teclas[-1] in ["+", "-", "*", "/"]:
        messagebox.showerror("Error", "Operacion incompleta")
        return

    lista_teclas = "".join(lista_teclas)

    try:
        resultado = eval(lista_teclas)  
        etiqueta_resultado.config(text=resultado)
    except ZeroDivisionError:
        messagebox.showerror("Error", "No se puede dividir por cero")
    
    lista_teclas = list(lista_teclas) 



boton_1 = Button(frame_teclas, text="1", width=5, height=2, bg="#ffffff", fg="#000000", command=agregar_1)
boton_1.grid(row=0, column=0, padx=5, pady=5)

boton_2 = Button(frame_teclas, text="2", width=5, height=2, bg="#ffffff", fg="#000000", command=agregar_2)
boton_2.grid(row=0, column=1, padx=5, pady=5)

boton_3 = Button(frame_teclas, text="3", width=5, height=2, bg="#ffffff", fg="#000000", command=agregar_3)
boton_3.grid(row=0, column=2, padx=5, pady=5)

boton_4 = Button(frame_teclas, text="4", width=5, height=2, bg="#ffffff", fg="#000000", command=agregar_4)
boton_4.grid(row=1, column=0, padx=5, pady=5)

boton_5 = Button(frame_teclas, text="5", width=5, height=2, bg="#ffffff", fg="#000000", command=agregar_5)
boton_5.grid(row=1, column=1, padx=5, pady=5)

boton_6 = Button(frame_teclas, text="6", width=5, height=2, bg="#ffffff", fg="#000000", command=agregar_6)
boton_6.grid(row=1, column=2, padx=5, pady=5)

boton_7 = Button(frame_teclas, text="7", width=5, height=2, bg="#ffffff", fg="#000000", command=agregar_7)
boton_7.grid(row=2, column=0, padx=5, pady=5)

boton_8 = Button(frame_teclas, text="8", width=5, height=2, bg="#ffffff", fg="#000000", command=agregar_8)
boton_8.grid(row=2, column=1, padx=5, pady=5)

boton_9 = Button(frame_teclas, text="9", width=5, height=2, bg="#ffffff", fg="#000000", command=agregar_9)
boton_9.grid(row=2, column=2, padx=5, pady=5)

boton_0 = Button(frame_teclas, text="0", width=5, height=2, bg="#ffffff", fg="#000000", command=agregar_0)
boton_0.grid(row=3, column=1, padx=5, pady=5)

boton_suma = Button(frame_teclas, text="+", width=5, height=2, bg="#ffffff", fg="#000000", command=agregar_suma)
boton_suma.grid(row=0, column=3, padx=5, pady=5)

boton_resta = Button(frame_teclas, text="-", width=5, height=2, bg="#ffffff", fg="#000000", command=agregar_resta)
boton_resta.grid(row=1, column=3, padx=5, pady=5)

boton_multiplicacion = Button(frame_teclas, text="*", width=5, height=2, bg="#ffffff", fg="#000000", command=agregar_multiplicacion)
boton_multiplicacion.grid(row=2, column=3, padx=5, pady=5)  

boton_division = Button(frame_teclas, text="/", width=5, height=2, bg="#ffffff", fg="#000000", command=agregar_division)
boton_division.grid(row=3, column=3, padx=5, pady=5)

boton_igual = Button(frame_teclas, text="=", width=5, height=2, bg="#ffffff", fg="#000000", command=lambda: calcular(lista_teclas))
boton_igual.grid(row=3, column=2, padx=5, pady=5)

boton_limpiar = Button(frame_teclas, text="C", width=5, height=2, bg="#ffffff", fg="#000000",  command= lambda:borrar(lista_teclas))
boton_limpiar.grid(row=3, column=0, padx=5, pady=5)

frame_espacio = Frame(ventana_calcular, width=250, height=60)
frame_espacio.place(relx=0.5, rely=0.15, anchor="center")
frame_espacio.configure(bg="#FFFFFF")

etiqueta_expresion = Label(frame_espacio, text=lista_teclas, width=20, height=1, bg="#ffffff", fg="#000000", font=("Arial", 10))
etiqueta_expresion.place(relx=0.35, rely=0.35, anchor="center")

etiqueta_resultado = Label(frame_espacio, text="", width=10, height=1, bg="#ffffff", fg="#000000", font=("Arial", 10))
etiqueta_resultado.place(relx=0.8, rely=0.75, anchor="center")

ventana_calcular.mainloop()