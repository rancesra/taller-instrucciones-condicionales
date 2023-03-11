# programa No. 2 

print ("--------------------------")
print (" AUTORIZACION PRESTAMO BANCARIO")
print ("--------------------------")

# input

sueldo = int(input("Escriba el valor de sus ingresos mensuales: "))
deudas = input("Tiene otros prestamos o deudas con otros bancos (responder si o no): ")

# validacion
if(sueldo>945200):
    if(deudas == "Si" or "si" or "SI"):
        print ("--------------------------")
        print("Tiene credito aprobado")
        print ("--------------------------")
    else:
        print ("--------------------------")
        print("No podemos autorizarle un credito")
        print ("--------------------------")
else:
    print ("--------------------------")
    print("No podemos autorizarle un credito")
    print ("--------------------------")