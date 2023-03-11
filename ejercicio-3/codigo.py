# verificar si un numero es mayor que otro


print("-----------------------------------------------")
print("------------Calcular Precio Venta--------")
print("-----------------------------------------------")

#input
PrecioCosto = int(input("Ingrese el costo base del producto: "))
PrecioFinal = int()
print("-------------------------------")
print("-------------------------------")

#condicion o validacion
print("-------------------------------")
print("------------RESULTADO----------")
print("-------------------------------")
if (PrecioCosto>3000):
    if(PrecioCosto<6000):
        PrecioFinal = PrecioCosto + 500
    else:
        PrecioFinal = PrecioCosto + (PrecioCosto*25)/100
else:
    PrecioFinal = PrecioCosto + (PrecioCosto*15)/100

# output
print(str(PrecioFinal))