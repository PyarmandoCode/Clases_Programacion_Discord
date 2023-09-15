#Crear Un programa que calcule el indice masa corporal(IMC)

peso = float(input("Ingrese su peso [kg]:"))
altura = float(input("Ingrese su Altura [m]:"))

imc = peso / (altura **2)

if imc <18.5:
    print("Bajo de Peso")
elif imc <24.9:
    print("Peso Normal")    
elif imc <29.9:
    print("Sobrepeso")    
else:
    print("Obeso")    