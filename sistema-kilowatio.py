kwh = int(input("ingresa el consumo mensual de kilowatios(kWh)"))

if kwh >=0 and kwh <=100:
    print("|Reporte|")
    print("|categoria| = bajo")
    print(f"|total a pagar| = {kwh*450}$")
    print("|Recomendacion| Exelente ahorro energetico")
    
elif kwh >= 101 and kwh <= 200:
    print("|Reporte|")
    print("|Categoria| Medio")
    print(f"|total a pagar| {kwh*500}$")
    print("|Recomendacion| consumo normal")
    
elif kwh >= 201 and kwh <= 350:
    print("|Reporte|")
    print("|Categoria| Alto")
    print(f"|Total a pagar| {kwh*650}$")
    print("|Recomendacion| considere reducir el uso electrodomestico")

else:
    print("|Reporte|")
    print("|Categoria| Critico")
    print(f"|Total a pagar| {kwh*800}$")
    print("|Recomendacion| ALERTA: Consumo excesivo. Revise fugas o desconecte equipos ")
