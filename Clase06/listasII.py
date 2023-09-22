#Suma elementos de una lista

#Funcion que recibe como argumento una lista para retornar la suma de sus elementos
def suma_elementos(lista):
    suma =sum(lista)
    return suma


lista_numeros = [20,56,78,120,45]
paises = {"chile":"santiago","bolivia":"lapaz"}
resultado= suma_elementos(lista_numeros)
print(f"La Suma de los elementos de la lista es {resultado}")
