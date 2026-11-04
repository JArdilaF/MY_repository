import numpy as np

A = np.array([
    [55, 1, 0, 0, 0],
    [75, -1, 1, 0, 0],
    [60, 0, -1, 1, 0],
    [75, 0, 0, -1, 1],
    [90, 0, 0, 0, -1]
])

B = np.array([449, 627, 453, 591, 792])

detA = np.linalg.det(A)
print(f"Determinante de A = {detA:.2f}")

if detA == 0:
    print("El sistema no tiene solución única.")
else:
    soluciones = []
    for i in range(5):
        Ai = A.copy()
        Ai[:, i] = B
        detAi = np.linalg.det(Ai)
        xi = detAi / detA
        soluciones.append(xi)
    print("Soluciones:")
    for i, x in enumerate(soluciones, start=1):
        print(f"x{i} = {x:.2f}")
