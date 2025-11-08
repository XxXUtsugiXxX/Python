#'''3. Gimnasio “Solo Leveling Fit” — Motivación + Bono'''
#'''Pedir cuántos días entrenó esta semana.

#    ≥ 4 días → "¡Excelente disciplina!" + gana 1 punto de energía
#    2 o 3 → "Bien, pero puedes dar más"
#    0 o 1 → "No aflojes, tú puedes mejorar
#    Mostrar mensaje y si aplica, los puntos ganados.

Dias_entrenados = int(input("digita el numero de días entrenados: "))
puntos = 0
while Dias_entrenados < 0:
    Dias_entrenados = int(input("edad invalida dijite otra: "))
if Dias_entrenados >= 4:
        puntos =+ 1
        print(f"¡Excelente disciplina! gana 1 punto de energía, tienes: {puntos} puntos")
elif Dias_entrenados == 2 or Dias_entrenados == 3:
        print(f"Bien, pero puedes dar más, animates mas de momento tienes: {puntos}")
else:
        print(f"No aflojes, tú puedes mejorar {puntos} puntos")