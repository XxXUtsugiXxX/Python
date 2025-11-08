#'''2. Cine “La Estrella” — Tarifas por edad
edad = int(input("introduce tu edad: "))
while edad < 0:
    edad = int(input("edad invalida dijite otra: "))
if edad <= 5 and edad >= 0:
    print(f"tu edad es {edad} puedes entrar gratis")
elif edad > 5 and edad <= 11:
    print(f"tu edad es {edad} y tu boleta vale $5.000")
elif edad >=12 and edad <=59:
     print(f"tu edad es {edad} y tu boleta vale $8.000")
else:
    print(f"tu edad es {edad} y tu boleta vale $4.000 (descuento adulto mayor)")