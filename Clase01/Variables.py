
import keyword
#print(keyword.kwlist)

#Ejemplo de Variables

"""DocString
Comentario en 
Varias Lineas
"""

edad_persona = 27 #int
nombre_persona ="Manuel" #str
curso_aprendio='Python' #str
costo_curso=20.78 #float
curso_activo=True #boolean
horas_curso = 19 #int

#Funciones Basicas
#print("Hola Mundo desde la Clase 1")
#valor=input("Ingrese un Valor por teclado:")
#print("El Valor que ud ingreso fue:"+valor)

#Formatos de Concatenacion
#print(nombre_persona+"Estudia el curso de"+curso_aprendio) #Forma1
#print(nombre_persona,"Estudia el curso de",curso_aprendio) #Forma2
#print(f"{nombre_persona} Estudia el curso de {curso_aprendio}" ) #Forma3

#castear datos
#print(f"La Persona  {nombre_persona} tiene {edad_persona} años")

# pago_hora=20 #const
# total_horas=int(input("Ingrese el total de horas Trabajadas:"))
# pago_jornal =total_horas*pago_hora
# print(f"El Pago a recibir es {pago_jornal}")

#Calcular er precio de compra por un producto incluyendo descuento e impuesto
desc=0.02
imp=0.18
precio=float(input("Ingrese el precio del producto:"))
cantidad=int(input("Ingrese la cantidad del producto:"))
total = precio*cantidad
total_des= total * desc
total_neto = total - total_des
total_imp = total_neto * imp
neto = total_neto + total_imp
print(f"El total a pagar es {neto} {total_imp} {total_neto}")
