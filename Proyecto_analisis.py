import sys

# Constantes
P_ESTATICA = 106230.0  
RHO_AGUA = 1000.0     
P_MAX_SEGURA = 300000.0 

#Función de Conversión
def pa_a_psi(pascales):
    return pascales / 6894.76

#Entrada de Datos
try:
    v_input = input("Ingrese la velocidad (m/s) a la cual fluye el agua: ")
    v = float(v_input)
    if v < 0:
        print("La velocidad no puede ser negativa. Usando valor absoluto.")
        v = abs(v)
except ValueError:
    print(" Error: Entrada inválida. Debe ingresar un número para la velocidad.")
    sys.exit() 

#Cálculo de Presión 
p = P_ESTATICA - (RHO_AGUA / 2) * (v**2)

# Salida de Resultados
print("\n" + "=" * 40)
print("               RESULTADOS ")
print("=" * 40)

print(f"Velocidad ingresada (v): {v:.2f} m/s")
print(f"La presión del agua es:   {p:.2f} Pa")
print(f"Equivalente a:            {pa_a_psi(p):.3f} PSI")

# Verificación de Seguridad 
print("-" * 40)
if p > P_MAX_SEGURA:
    print("¡ADVERTENCIA DE PRESIÓN ALTA! El valor supera el límite seguro de diseño.")
    print(f"Límite de seguridad: {P_MAX_SEGURA} Pa")
elif p < 0:
    print("¡ADVERTENCIA! Presión negativa. Posible vacío o succión.")
else:
    print("Presión dentro del rango de operación seguro.")
print("=" * 40)