import time

numero=int(input("Ingrese un numero para comenzar la cuenta regresiva:"))

while numero >=0:
    print(numero)
    time.sleep(1)
    numero -=1
print("Cuenta Regresiva Completa")    