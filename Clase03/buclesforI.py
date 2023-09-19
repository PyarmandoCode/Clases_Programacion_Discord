# for pos in range(1,11,2):
#     #dentro del bucle
#     print(f" {pos} Bienvenido a python")
# print("***FIN DEL BUCLE***")    


# mi_lista=[1,True,["FLASK","DJANGO","FASTAPI"],4.0,"PYTHON"]

# for elemento in mi_lista:
#     print(elemento)


# n = int(input("Ingresa el Limite de los numeros:"))#10
# suma = 0 #acumulador
# for i in range(1,n+1):#10
#     suma +=i
# print(f"La Suma es: {suma}")    

# texto="Python"
# for letra in texto:
#     print(letra)


tot=0
cont=0
precios=[1200.80,1700.20,1800.50,34.90]    
for item in precios:
    if item>1800:
        break #Finalizar el bucle
    else:
        tot +=item #acumulando
    cont +=1
print(f"La cantidad a pagar sera {tot} y el numero de items es {cont}")    
