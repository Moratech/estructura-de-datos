# Programa de Inscripción de Alumnos de Universidad Privada

print("Inscripción de Alumnos - Universidad Privada")

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
fecha_nacimiento = input("Ingrese su fecha de nacimiento (dd/mm/yyyy): ")

posee_titulo_secundario = True

monto_matricula = float(input("Ingrese el monto de la matrícula: "))

cuota = monto_matricula + 1000

arancel_python = 12000

costo_mensual = cuota + (arancel_python / 4)

descuento_efectivo = costo_mensual * 0.15
costo_con_descuento = costo_mensual - descuento_efectivo

print("\n----- Datos del Alumno -----")
print(f"Nombre: {nombre}")
print(f"Edad: {edad}")
print(f"Fecha de Nacimiento: {fecha_nacimiento}")
print(f"Posee título secundario: {posee_titulo_secundario}")
print(f"Monto de la matrícula: ${monto_matricula:.2f}")
print(f"Cuota (incluye $1000 adicionales): ${cuota:.2f}")
print(f"Arancel Python I (por cuatrimestre): ${arancel_python:.2f}")
print(f"Costo mensual total: ${costo_mensual:.2f}")
print(f"Costo con descuento por pago en efectivo: ${costo_con_descuento:.2f}")



