carrito = {}

#Funcion para agregar un producto al carrito
def agregar_producto(producto,precio):
    if producto in carrito:
        carrito[producto] +=precio#acumular el precio
    else:
        carrito[producto] =precio


#Funcion para mostar el contenido del carrito
def mostrar_carrito():
    total=0
    print("Carrito de compras")        
    for producto,precio in carrito.items():
        print(f"{producto}: ${precio}")
        total +=precio #acumulador
    print(f"Total: ${total}")    

def main():
    while True:
        print("\nOpciones")
        print("1.Agregar un Producto al carrito")
        print("2.Mostrar el carrito")
        print("3.Salir")

        opcion=input("Seleccione una opcion:")

        if opcion == "1":
            producto = input("Ingrese el nombre del Producto:")
            precio = float(input("Ingrese el Precio del Producto:"))
            agregar_producto(producto,precio)
            print(f"{producto} ha sido agregado al carrito")

        elif opcion =="2":
            mostrar_carrito()
        elif opcion == "3":
            print("Gracias por comprar con nosotros. Hasta Luego!")    
            break
        else:
            print("Opcion no es valida por favor seleccione otra opcion")