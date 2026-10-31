'''
/*
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
 */
'''

def area(n):
    if n == 1:
        h = int(input("escriba el valor de la altura del triangulo:\n"))
        b = int(input("escriba el valor de la base de su triangulo:\n"))
        a = (h * b)/2
        return a 
    if n == 2:
        l = int(input("escriba el valor de uno de los lados de su cuadrado:\n"))
        a = l**2
        return a 
    if n == 3:
        h = int(input("escriba el valor de la altura de su rectangulo:\n"))
        b = int(input("escriba el valor de la base de su rectangulo:\n"))
        a = h * b
        return a 

print("""
A cual de los siguientes poligonos desea obtener su area:
    
    [1] Triangulo
    [2] Cuadrado
    [3] Rectangulo
      """)

n = int(input('\n'))

while n < 1 or n > 3:
    print('poligono no existe')
    n = int(input('\n'))

print(f'el area de su poligono es: {area(n)} u^2')