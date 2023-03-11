# programa para determinar si un numero es multiplo del otro

print("-----------------------------------------")
print("----------DETERMINAR EL MULTIPLO---------")
print("-----------------------------------------")

# INPUT

a=int(input("ingrese el primer valor: "))
b=int(input("ingrese el segundo valor: "))

# PROCESSING

c= a%b
if c == 0:
    d=b%a
    if d == 0:
        rta= f"{a} es igual a {b}"
    else:
        rta=f"{a} es multiplo de {b}"
else:
    d=b%a
    if d == 0:
        rta = f"{b} es multiplo de {a}"
    else:
        rta=f"{a} y {b} no son multiplos"

# OUTPUT

print("-------------------------------------------")
print("-------------EL RESULTADO ES---------------")
print(rta)
print("-------------------------------------------")