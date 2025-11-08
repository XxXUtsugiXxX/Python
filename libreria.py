#5. Librería “El Saber” — Descuento estudiante + cupón

#Libro cuesta $25.000.

  #  Si es estudiante → 15% descuento
 #   Si además tiene cupón "LIBRO10" → 10% adicional sobre el valor ya descontado

#Validar:

  #  Si no es estudiante, el cupón no aplica.
 #   Si ingresa cupón incorrecto, ignorarlo.
#
#Mostrar total.

estudiante = int(input("si eres estudiante digita 1, si no digita 2: "))
libro = 25000
descuento = libro * 0.15
descuento2 = libro * 0.75
cupon = str()
while estudiante <1 or estudiante >2:
    estudiante = int(input("dijita solo 1 o 2: "))
if estudiante == 1:
    print("el precio de tu libro es de: ", libro - descuento)
    cupon = input("tienes cupon de descuento?, en caso de que si digitalo: ")
    if cupon == "LIBRO10":
        print("el precio de tu libro es de: ", descuento2)
    else:
        print("El precio de tu libro es de: ", descuento)
else:
    print("El precio de tu libro es de: ", libro)