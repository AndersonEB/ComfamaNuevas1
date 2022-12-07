numeroM =  float(input("Digita el numero:  "))

if numeroM % 5 == 0:
    print("El numero ingresado es multiplo de 5")
elif numeroM % 3 == 0:
    print("El numero ingresado es multiplo de 3")
else:
    print("El numero ingresado no es multiplo de 5 y tampoco es multiplo de 3")