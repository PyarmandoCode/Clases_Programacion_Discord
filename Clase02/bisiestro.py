año = int(input("Ingrese año:"))
if (año % 4 == 0 and año % 100!=0) or (año % 400 ==0):
    print(f"El año {año} es Bisiestro")
else:
    print(f"El año {año} no es Bisiestro")    
