# programa No. 4

print ("--------------------------")
print (" calcular índice de masa corporal(IMC)")
print ("--------------------------")

#input

peso = int(input("Escriba su peso corporal en kg: "))
altura = float(input("Escriba su altura en m(metros): "))

#calculo imc

imc = peso/altura**2

#validacion
if(imc<16):
    rta = ("Criterio de ingreso en hospital")
else:
    if(16<imc<17):
        rta = ("Infrapeso")
    else:
        if(17<imc<18):
            rta = ("Bajo peso")
        else:
            if(18<imc<25):
               rta = ("Peso normal (saludable)")
            else:
                if(25<imc<30):
                    rta = ("Sobrepeso (obesidad grado I)")
                else:
                    if(30<imc<35):
                        rta = ("Sobrepeso crónico (obesidad grado II)")
                    else:
                        if(35<imc<40):
                            rta = ("Obesidad premórbida (obesidad grado III)")
                        else:
                            rta = ("Obesidad mórbida (obesidad de grado IV)")

print(str(rta))