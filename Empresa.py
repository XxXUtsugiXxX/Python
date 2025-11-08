#8. Empresa “TecnoPlus” — Evaluación compuesta

#El usuario ingresa dos notas (0.0 - 5.0):

  #  Prueba técnica (70%)
 #   Prueba lógica (30%)

#Cálculo: nota_final = (tecnica * 0.7) + (logica * 0.3)

#Condiciones:

   # nota_final ≥ 3 → “Aprobado”
  #  2 ≤ nota_final < 3 → “Revisión”
 #   < 2 → “Reprobado”

#Validar que las notas estén en rango.

'''nota_tecnica = float(input("ingresa la nota sacada en la prueba tecnica solo de 0.0 a 5.0: "))
while nota_tecnica < 0.0 or nota_tecnica > 5.0:
    nota_tecnica = float(input("dijita una nota correcta: "))

nota_logica = float(input("ingresa la nota de la prueba logica solo de 0.0 a 5.0: "))
while nota_logica < 0.0 or nota_logica > 5.0:
    nota_logica = float(input("dijita una nota correcta: "))
calculo_nota_final = (nota_tecnica * 0.7) + (nota_logica * 0.3)

if calculo_nota_final >= 3:
    print ("Aprobado, tu nota es: ", calculo_nota_final)
elif calculo_nota_final >= 2 or calculo_nota_final < 3:
    print("Revisión, tu nota es: ", calculo_nota_final)
else:
    print("Reprobado,  tu nota es: ", calculo_nota_final)'''