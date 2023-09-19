numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
elemento_buscado=int(input("Cual es el elemnto a buscar:"))
for numero in numeros:
    if numero==elemento_buscado:
        print(f"encontre  {elemento_buscado} en la lista")
        break
else:
    print(f"{elemento_buscado} no esta en la lista")
        

