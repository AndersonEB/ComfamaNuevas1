opcion = 100
print("Empanadas el machetico")
print("**********************\n")

print("1. registrar empanadas ")
print("2. ver empanada  ")
print("0. salir")
empanadas = []
while opcion != 0:
    opcion = int(input("Digite una opcion"))
    if opcion==1:
        empanada=input("Digite el nombre de la empanada a registrar: ")
        empanadas.append(empanada)    
    elif opcion==2:
        for empanada in empanadas:
            print(f'La empanada seleccionada es: {empanada}')
    elif opcion==0:  
        break
    else:
        print("No ha seleccionado una opcion valida")

#agregar al menu una opcion que elimine el ultimo elemento agregado a la lista