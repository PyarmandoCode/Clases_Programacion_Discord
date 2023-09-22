saldo = 1000

while True:
    print(f"Saldo Actual {saldo}")
    print("Operaciones Disponibles")
    print("1.-Deposito")
    print("2.-Retiro")
    print("3.-Salir")

    opcion = input("Elige una operacion o presiona la tecla 3 para salir:")

    if opcion=="3":
        print("Gracias por Utilizar Nuestro cajero Automatico")
        break #False

    if opcion in ("1","2"):
        cantidad = float(input("Ingrese la cantidad:"))

        if opcion =="1":
            saldo +=cantidad
            print(f"Deposito Exitoso . Saldo Actual {saldo}")
        elif opcion =="2":
            if cantidad <=saldo:
                saldo -=cantidad    
                print(f"Retiro Exitoso . Saldo Actual {saldo}")
            else:
                print("Saldo Insuficiente") 
    else:
        print("Opcion Invalida")               



    
