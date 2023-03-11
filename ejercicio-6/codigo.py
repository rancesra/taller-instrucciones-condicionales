# programa 6

import math

#coeficientes de la ecuación cuadrática
a = float(input("Ingrese el coeficiente a: "))
b = float(input("Ingrese el coeficiente b: "))
c = float(input("Ingrese el coeficiente c: "))

#discriminante
discriminante = b**2 - 4*a*c

# validacion
if discriminante > 0:
    # Dos raíces reales distintas
    x1 = (-b + math.sqrt(discriminante)) / (2*a)
    x2 = (-b - math.sqrt(discriminante)) / (2*a)
    print("Las raíces son:", x1, "y", x2)
else:
    if discriminante == 0:
        # Una raíz real doble
        x = -b / (2*a)
        print("La raíz doble es:", x)
    else:
        #Dos raíces complejas
        realPart = -b / (2*a)
        imaginaryPart = math.sqrt(-discriminante) / (2*a)
        print("Las raíces son complejas:")
        print(realPart, "+", imaginaryPart, "i y", realPart, "-", imaginaryPart, "i")