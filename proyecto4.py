# Función para determinar el aula según el número de día
def determinar_aula(dia):
    if dia % 2 == 0:
        return "A-300"
    else:
        return "A-315"
def mostrar_listado_aulas():
    print("Día\tAula")
    for dia in range(1, 7):
        aula = determinar_aula(dia)
        print(f"{dia}\t{aula}")
mostrar_listado_aulas()

# Cargar edades válidas (mayores de edad)
def cargar_edades():
    errores = 0
    while True:
        try:
            edad = int(input("Ingrese una edad (mayor o igual a 18, -1 para salir): "))
            if edad == -1: 
                break
            elif edad >= 18:
                print(f"Edad ingresada: {edad}")
            else:
                print("Error: La edad ingresada es menor de edad.")
                errores += 1
        except ValueError:
            print("Error: Ingrese un valor numérico válido.")
            errores += 1
    print(f"Cantidad de cargas erróneas: {errores}")
cargar_edades()

# Cargar notas de 5 alumnos y calcular el promedio
def calcular_promedio_notas():
    total_notas = 0
    for i in range(1, 6): 
        while True:
            try:
                nota = float(input(f"Ingrese la nota del alumno {i}: "))
                if 0 <= nota <= 10:
                    total_notas += nota
                    break
                else:
                    print("Error: Ingrese una nota válida (0 a 10).")
            except ValueError:
                print("Error: Ingrese un valor numérico válido.")
    
    promedio = total_notas / 5
    print(f"El promedio de las notas es: {promedio:.2f}")
calcular_promedio_notas()

# Calcular el costo del comedor por la cantidad de días
def calcular_costo_comedor():
    costo_por_dia = 1250
    print("Días\tCosto Total")
    for dias in range(1, 7): 
        costo_total = dias * costo_por_dia
        print(f"{dias}\t${costo_total}")
calcular_costo_comedor()

