#Par o impar
num = int(input("Ingresa el numero 0:   "))
numfin = int(input("Ingresa el numero 1000:  "))

for i in range (num, numfin +1):
    if i % 2 == 0:
      print(i, "par")
    else:
      print(i, "impar")
