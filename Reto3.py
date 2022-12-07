#se desea recoger 20 numeros y almacenarlos en una lista y al final imprimimos la lista 

numeros = []
for numero in range(20):
    numeros.append(input("digita un numero:  "))
for numero in numeros:
    print(numero)

    