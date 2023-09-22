#Eliminar duplicados de una Lista

def eliminar_duplicados(lista):
    lista_sin_duplicados=list(set(lista))
    return lista_sin_duplicados


lista_con_duplicados=[1,2,2,3,4,4,5]
lista_sin_duplicados=eliminar_duplicados(lista_con_duplicados)
print(f"Lista sin Duplicados {lista_sin_duplicados}")


# datos = {12,18,18,19,20}
# print(datos)