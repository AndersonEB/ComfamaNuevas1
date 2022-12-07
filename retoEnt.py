#Construir un programa que reciba números enteros y los sume mientras estos sean positivos, si se digita un número negativo el programa debe terminar
numero1 = int(input("Digita un numero:  "))

if (numero1>=0): 
    numero2 = int(input("Digita otro numero: "))
    
    if (numero2>=0):
        print(numero1+numero2)

    else:
        print("fin del programa")
    
    
else:
    print("fin del programa")



