##Codificar un programa que presente un menú de 4 opciones y reciba un numero natural  para realizar las siguientes operaciones0: Salida 1: Encuentre si el número es múltiplo de 2 2: Encuentre la raíz cuadrada del número 3: Sume 100 al número ingresado 4: Eleve a la 2 el número ingresado
from cmath import sqrt
numero = 1
print("********************")
print("      MENU          ")
print("********************")
print(" 0: Salida")
print(" 1: Encuentre si el número es múltiplo de 2") 
print(" 2: Encuentre la raíz cuadrada del número ")
print(" 3: Sume 100 al número ingresado")
print(" 4: Eleve a la 2 el número ingresado")
while (numero!=0):
    numero = int(input("Digite una opcion del menú: "))
    if (numero == 1): 
            numero = float(input("Digite un numero: "))
            if (numero %2==0):
                print("el numero ", numero, "es multiplo de 2 ")
            else:
                print("El numero ", numero, "no es multiplo de 2 " )
    elif(numero == 2):
             numero = float(input("Digite un numero: "))     
             print("la raiz cuadrada de ",numero, "es:, ", (sqrt(numero)))
    elif(numero == 3):
             numero = float(input("Digite un numero: "))     
             print("El numero ",numero, "más 100, es:, ", (numero + 100))
    elif(numero == 4):
             numero = float(input("Digite un numero: "))     
             print("El numero ",numero, " elevado a la 2 es:, ", (numero ** 2))  
    
else: 
    print("Eligió salir del menú")

