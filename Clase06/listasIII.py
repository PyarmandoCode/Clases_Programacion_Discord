#Encontrar el numero mas grande y el mas pequeño de una lista


def encontrar_extremos(lista):
    maximo=max(lista)
    minimo=min(lista)
    return maximo,minimo

lista_numeros = [20,56,78,120,45]

maximo,minimo =encontrar_extremos(lista_numeros)
print(f"El Valor Maximo y Minimo es {maximo} {minimo}")