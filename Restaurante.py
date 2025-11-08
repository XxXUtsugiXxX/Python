#7. Restaurante “El Sabor Colombiano” — Menú + bebida opcional + IVA

#Menú: $12.000

#Opciones bebida:

 #   sí → $3.000
  #  no → $0

#Luego aplicar IVA del 8% al total final.
#Mostrar valor con IVA incluido.

menu = 12000
tomar = 3000
menu_tomar = menu + tomar
print("bienvenido al restaurante el sabor de colombia")
print("el menu del día vale: $12000, sin iva incluido")
bebida = str(input("quieres bebida, si o no: ")).lower()
while bebida != "si" and bebida != "no":
    bebida=str(input("digita si o no: ")).lower()
if bebida == "si":
    print("el valor de la bebida es: $3000")
    print("el valor total sin iva incluido es de: ", menu + tomar)
    iva = (menu + tomar) * 0.08 + menu_tomar
    print("el valor total con iva incluido es de: ", iva)
else:
    iva = menu * 0.08 + menu
    print("el valor total con iva incluido es de: ", iva)