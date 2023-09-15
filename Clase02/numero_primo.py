"""
Operadores Matematicos
+ - * **
/ //
% residuo mod
"""
numero = int(input("Ingrese un numero:"))
if numero >1:
    for i in range(2,numero):
        if (numero % i) == 0:
            print(f"numero {numero} no es primo")
            break
    else:
        print(f"numero {numero} es primo")    
else:
    print(f" numero {numero} no es primo ni par")        

