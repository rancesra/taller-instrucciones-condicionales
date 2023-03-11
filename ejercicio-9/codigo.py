# TRIANGULOS

ladoa = int(input("escriba el lado A: "))
ladob = int(input("escriba el lado B: "))
ladoc = int(input("escriba el lado C: "))

#validacion

if(ladoc**2 < ladoa**2+ladob**2):
    rta = "el triangulo es agudo"
elif(ladoc**2 ==  ladoa**2+ladob**2):
    rta = "el triangulo es recto"
elif(ladoc**2 > ladoa**2+ladob**2):
    rta = "El triangulo es obtuso"
print(str(rta))
