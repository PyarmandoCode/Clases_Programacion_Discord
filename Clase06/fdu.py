def suma_elementos(lista):
    suma =sum(lista)
    return suma

def encontrar_extremos(lista):
    maximo=max(lista)
    minimo=min(lista)
    return maximo,minimo

def eliminar_duplicados(lista):
    lista_sin_duplicados=list(set(lista))
    return lista_sin_duplicados