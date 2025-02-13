#El ultimo  que ingresa es el primero en salir
nombres = []

for i in range (5):

    nombre = input("Ingresa  un nombre:   ")
    nombres.append(nombre)

#nombres = [nombres[-1]] + nombres[1:-1] + [nombres[0]]
nombres.reverse()
print ("Los nombres son ordenados, el ultimo es el primero y el primero es el ultimo:    ")
for nombre in nombres:
           print (nombre)
