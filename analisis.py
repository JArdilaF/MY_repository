print("Para la ecuacion 1")
x1 = int(input("Digite el coeficiente 1: \n"))
y1 = int(input("Digite el coeficiente 2: \n"))
ti1 = int(input("Digite el termino independiente: \n"))

print("Para la ecuacion 2")
x2 = int(input("Digite el coeficiente 1: \n"))
y2 = int(input("Digite el coeficiente 2: \n"))
ti2 = int(input("Digite el termino independiente: \n"))


matriz = [[x1, y1, ti1],
          [x2, y2, ti2]]

print(matriz)


pivote = matriz[0][0]
for j in range(3):
    matriz[0][j] /= pivote

factor = matriz[1][0]
for j in range(3):
    matriz[1][j] -= factor * matriz[0][j]

pivote = matriz[1][1]
for j in range(3):
    matriz[1][j] /= pivote

factor = matriz[0][1]

for j in range(3):
    matriz[0][j] -= factor * matriz[1][j]
    
x = matriz[0][2]
y = matriz[1][2]

print(f"La solución es: x = {x}, y = {y}")
