# programa No. 5

print ("--------------------------")
print ("Calcular el gasto de agua")
print ("--------------------------")

#input

agua = int(input("Digite la cantidad de agua gastada en m^3: "))

#validacion

if(agua<50):
    costot = "Debe pagar 1000"
else:
    if(agua<200):
        costot = (agua-50)*2000+1000
    else:
        if(agua>=200):
            costot = (agua-50)*3000+1000
        else:
            ("codigo mal")
print(str(costot))
