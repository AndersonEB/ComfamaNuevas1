#Una compañía de software contable, paga a su personal de ventas un salario de 3500000 mensuales, mas una comisión de 1500000 por cada licencia de software vendida menos el (5% del salario total + comisiones de deducciones) por impuestos. Codifica un programa que calcule e imprima el salario mensual de un vendedor dado recibiendo el numero de ventas realizadas
salM = 3500000
venRZ = int(input("digite el numero de ventas realizadas:  "))
com  =  (venRZ * 1500000)
salTl = (salM + com)*0.95
print("Salario Base: ", salM)
print("Total comision por ventas: ", com)
print (" sueldo total despues de deducciones: ", salTl)