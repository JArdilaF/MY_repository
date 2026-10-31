'''
/*
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
'''

# forma NO recursiva 

''''
n = int(input("cuantos numeros de la sucesion de Fibonacci quiere imprimir?\n"))

sucesion = [0, 1]

for i in range(n-2):
    x = sucesion[i] + sucesion[i+1]
    sucesion.append(x)

print(sucesion)
'''

#Forma recursiva

def sucecion(n):
    v = [0, 1]
    if n == 2:
        return v
    else:
        v = sucecion(n-1)
        v.append(v[-1] + v[-2])
        return v
    
n = int(input("cuantos numeros de la sucesion de Fibonacci quiere imprimir?\n"))
print(sucecion(n))