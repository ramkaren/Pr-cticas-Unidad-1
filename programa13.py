#Iteracion de numeros 1000 a 0
num = int(input("Ingresa el numero 1000:  "))
num_final = int(input("Ingresa el numero 0:  "))

paso = 3

for i in range (num, num_final, -paso):
    print(i)
