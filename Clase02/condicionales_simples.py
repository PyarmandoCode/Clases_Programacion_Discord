#Operadores Logicos
"""
>
<
>=
<=
==
and = y
or = O
not =NEGACION
"""

edad = int(input("Ingrese la edad de la persona:"))
if edad >=18:
    #Bloque de codigo cuando sea Verdad
    dosis=int(input("Ingrese las dosis de vacuna:"))
    if dosis>=2 and dosis<=3:
        print("Usted cumple con todos los requsitos")
    else:
        print("usted no cumple con las dosis dispuestas")    
else:
    #Bloque de codigo cuando sea Falso
    print("La Persona es Menor de edad")    