 #9. Supermercado “AhorroMax” — Descuentos y envío

#Cada producto cuesta $2.000.

#Reglas:

#        30 unidades → 15% descuento
#
 #       10 unidades → 5% descuento
#
#    Si el total después del descuento es < $50.000 → agregar $5.000 de envío

#Calcular total final.
print("recuerda que si compras 10 productos tienes 5% de descuento y si son 30 tienes el 15%")
print("por compras inferiores a 50000 se cobran 5000 de envio")
productos = int(input("ingresa la cantidad de productos que compraste: "))
precio = 2000
cantidad = precio * productos
descuento30 = cantidad * 0.85
descuento10 = cantidad * 0.95
if cantidad < 50000:
    descuento10 = descuento10 + 5000
    print("el precio total a pagar es", descuento10)
else:
    print("la cantidad a pagar es de: ", descuento30)