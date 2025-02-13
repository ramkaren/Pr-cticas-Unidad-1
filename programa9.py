#Numero de las letras de una palabra
pal = input ("Ingresa una palabra:   ")
conteo = 0
for caracter in pal:
  if caracter.isalpha():
    conteo += 1
print("El numero de  letras en una palabra es:  ", conteo)
