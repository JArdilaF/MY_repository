'''
Escribe una función que reciba dos palabras (String) y retorne
  verdadero o falso (Bool) según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS
  las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
 - Dos palabras exactamente iguales no son anagrama.
'''

p1 = input("Escribe tu primera palabra: \n").strip()
p2 = input("Escribe tu segunda palabra: \n").strip()

def anagrama(p1, p2):
    return sorted(p1.lower()) == sorted(p2.lower())

print(anagrama(p1, p2))