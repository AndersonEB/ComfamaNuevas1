#ENTRADAS DEL POBLEMA

nivelAgua = int(input("Digita el nu¿ivel de agua:  "))
#EVALUANDO CAMINOS MÚLTIPLES
if nivelAgua <= 100:
    print("Bajo nivel de agua")
elif nivelAgua > 100 and nivelAgua < 400:
    print("Operación Optima")
elif nivelAgua >= 400:
    print("peligro!!")
else:
    print("Nivel de agua no valido")