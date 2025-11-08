#Panadería de Don Pancho — Descuentos por cantidades
#'''La panadería de Don Pancho vende pan a $300 cada uno.

#Reglas:

 #   Si compra más de 20 panes → 10% descuento
  #  Si compra más de 50 panes → 20% descuento
   # Si ingresa una cantidad negativa, mostrar "Cantidad inválida"

#Calcular y mostrar el total.'''

panes = int(input("Bienvenido, cuantos panes deseas llevar: "))
precio = 300
pago_total = 0
while panes < 0:
    panes = int(input("contidad invalida dijite otra cantidad: "))
if panes >= 1 and panes <=20:
    precio = panes * precio
    print(f"el pago total es: {precio}" )
elif panes > 20 and panes < 50:
    precio = panes * precio
    pago_total = (precio) * (10/100)
    pago_total = precio - pago_total
    print(f"el pago total es: {pago_total}" )
elif panes > 50 :
    precio = panes * precio
    pago_total = (precio) * (20/100)
    pago_total = precio - pago_total
    print(f"el pago total es: {pago_total}" )