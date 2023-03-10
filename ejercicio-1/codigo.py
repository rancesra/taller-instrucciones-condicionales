# verificar si un numero es mayor que otro


print("-----------------------------------------------")
print("------------PUNTOS DEL PLANO CARTESIANO--------")
print("-----------------------------------------------")

#input
x = int(input("INGRESE EL VALOR X: "))
y = int(input("INGRESE EL VALOR Y: "))
print("-------------------------------")
print("-------------------------------")

#condicion o validacion
print("-------------------------------")
print("------------RESULTADO----------")
print("-------------------------------")
if (x == 0):
    if(y == 0):
        msg = ("el punto esta en el origen")
    else:
        if(y>0):
            msg = ("el punto esta en el eje y")
        else:
            msg = ("el punto esta en el eje y")
else:
    if (x<0):
        if(y==0):
            msg = ("el punto esta sobre el eje x")
        else:
            if(y<0):
                msg = ("el punto esta en el tercer cuadrante")
            else:
                msg = ("el punto esta en el segundo cuadrante")
    else:
        if(y==0):
            msg = ("el punto esta sobre el eje x")

        else:
            if(y>0):
                msg = ("el punto esta en el primer cuadrante")
            else:
                msg = ("el punto esta en el cuarto cuadrante")

# output
print(str(msg))