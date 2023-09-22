#Colleciones de datos
#Listas
#Tuplas
#Diccionarios
#Sets

cursos=["python","flask","django",100,120.50,True,["java","golang"]] #list

#print(type(cursos))
#print(cursos[3])

# for elem in cursos:
#     print(elem)
# print("Fin de la lista")    
#CRUD
cursos.append("Angular") #añades al final
cursos.insert(2,"ReactJS") #añades x posicion
#print(cursos[2])#visualizar pos posicion
cursos[2]="ReactNative" #Actualizando el elemento por posicion
cursos.pop(2) #Eliminando Por Posicion
cursos.remove("django") #Eliminado por el Nombre
print(cursos)