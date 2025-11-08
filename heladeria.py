#4. Heladería “Frosty” — Sabor y topping
#Sabores y precios:

 #   chocolate → $4.000
  #  vainilla → $3.500

#Opcional: topping cuesta $1.000.

#Si el usuario ingresa un sabor que no existe, mostrar "Sabor no disponible".
#Si el sabor es válido, preguntar si quiere topping y calcular total.

print("tenemos estos precios y sabores:")
print("vainilla $3.500")
print("chocolate $4.500")
print("topping $1.000")
sabor_helado = str(input("dijita el sabor de helado que quieres ")).lower()
while sabor_helado != "vainilla" and sabor_helado != "chocolate":
    sabor_helado = str(input("Sabor no disponible, escoge otro: ")).lower()
if sabor_helado == "vainilla":
    topping = int(input("¿quieres un topping? si(1) o no(2) ")).lower()
    if topping == 1:
        print("el valor del helado con el topping es: ", 3.500 + 1.000)
    else:
        print("el valor es ", 3.500)
else: 
    topping = int(input("¿quieres un topping? si o no ")).lower()
    if topping == si:
        print("el valor del helado con el topping es: ", 4.500 + 1.000)
    else:
        print("el valor es ", 4.500)