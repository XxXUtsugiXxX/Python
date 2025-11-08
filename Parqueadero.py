
#Parqueadero “RapidCar” — Tarifa escalonada
#Tarifa:

  #  0 a 5 horas: $2.000 x hora

 #       5 horas: $2.000 x hora + multa fija de $5.000

#Validar horas:

 #   No permitir números negativos.

#Mostrar valor total.

horas = int(input("dijita el numero de horas que estuvo tu vehiculo: "))
while horas < 0:
    horas = int(input("hora invalida dijite otra que sea: ")).lower()
if horas >=0 and horas <= 5:
    print(f"la cantidad de horas es: {horas} y el valor del parqueadero es de: ", horas * 2000)
else:
    print(f"la cantidad de horas es: {horas} yel valor del parqueadero es de: ", horas * 2000 + 5000)