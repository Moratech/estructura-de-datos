# Función para determinar aula según el día
def determinar_aula(dia):
    if dia % 2 == 0:
        return "A-300"
    else:
        return "A-315"
def calcular_descuento(materias, turno, cuota):
    if turno.lower() == "tarde" and materias > 3:
        descuento = 0.25
    else:
        descuento = 0.05
    
    cuota_con_descuento = cuota - (cuota * descuento)
    return cuota_con_descuento
def calcular_estacionamiento(vehiculo):
    if vehiculo.lower() in ["auto", "moto"]:
        return 300
    elif vehiculo.lower() == "bicicleta":
        return 50
    else:
        return 0  
def main():
    dia = int(input("Ingrese el número del día (1 a 6, donde 1 es lunes y 6 es sábado): "))
    if 1 <= dia <= 6:
        aula = determinar_aula(dia)
        print(f"El aula asignada para el día {dia} es {aula}.")
    else:
        print("Día inválido.")
    materias = int(input("Ingrese el número de materias inscritas: "))
    turno = input("Ingrese el turno (Mañana/Tarde): ")
    cuota = float(input("Ingrese el valor de la cuota: "))
    cuota_con_descuento = calcular_descuento(materias, turno, cuota)
    print(f"El valor de la cuota con descuento es: {cuota_con_descuento:.2f}")
    vehiculo = input("¿Qué vehículo utiliza (Auto/Moto/Bicicleta/Ninguno)?: ")
    costo_estacionamiento = calcular_estacionamiento(vehiculo)
    if costo_estacionamiento > 0:
        print(f"El costo diario de estacionamiento es: ${costo_estacionamiento}")
    else:
        print("No se cobra estacionamiento.")
main()
