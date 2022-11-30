MesActual = input("digita el mes actual:   ")

if MesActual == "enero" or MesActual == "diciembre" or MesActual == "febrero":
    print("Estamos en invierno")
elif MesActual == "marzo" or MesActual == "abril" or MesActual == "mayo":
    print("Estamos en primavera")
elif MesActual == "junio" or MesActual == "julio" or MesActual == "agosto":
    print("Estamos en verano")
elif MesActual == "septiembre" or MesActual == "octubre" or MesActual == "noviembre":
    print("Estamos en otoño")
else: print("no digitaste ningún mes, intentalo de nuevo ")

   