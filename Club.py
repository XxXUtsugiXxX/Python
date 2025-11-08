#10. Club “Noche Estelar” — Acceso + validación documento

#Pedir edad y documento.

#Reglas:

 #   Edad ≥ 18 → puede entrar solo si tiene documento.
  #  Si la edad < 18 → "Entrada denegada"
   # Si tiene 18 o más pero no tiene documento → "Debe presentar documento"

documento = str(input("responde si o no, eres mayor de edad ")).lower()

while documento != "si" and documento != "no":
    documento = str(input("responde si o no: "))

if documento == "si":
    documento_muestra = str(input("muestra tienes el documento, si o no: ")).lower()

    while documento_muestra != "si" and documento_muestra != "no":
        documento_muestra = str(input("responde si o no ")).lower()
    if documento_muestra == "si":
        print("puedes entrar")
    else:
        print("debes presentar documento")

else:
    print("entrada denegada")