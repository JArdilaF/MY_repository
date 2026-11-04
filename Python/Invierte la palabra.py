v = "hola mundo" 

letras = []
for letra in v:
    letras.append(letra)

#print(letras)

letras.reverse()
#print(letras)

invertido = "".join(letras)
print(invertido)
