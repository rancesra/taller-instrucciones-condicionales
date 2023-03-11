# Dado 3 terminos saber si la suma de los dos primeros es igual al tercero

# INPUT

A = int(input("ingrese el valor de a: "))
B = int(input("ingrese el valor de b: "))
C = int(input("ingrese el valor de c: "))

D = A+B

# PROCESSING

if D==C :
    rta = ("La suma de a y b son iguales que C")
else: 
    rta = ("La suma de a y b no son iguales que C")

#OUTPUT

print("----------------------------------------")
print("-------------RESULTADO------------------")
print(rta)
PRINT("----------------------------------------")