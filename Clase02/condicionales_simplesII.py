total_compra=float(input("Ingrese el total de la compra:"))

if total_compra>100:
    descuento = total_compra*0.10
    total_con_descuento=total_compra-descuento
    print(f"Total con descuento(10%) {total_con_descuento}")
else:
    print(f"No se aplica descuento. Total a Pagar {total_compra}")    