# Función para obtener los resultados de las notas de los exámenes
def resultados_notas(nota1, nota2):
   
    promedio = (nota1 + nota2) / 2
    
    if nota2 >= 7:
        print("Aprobó el último examen.")
    else:
        print("Desaprobó el último examen.")
    if nota2 > nota1:
        print("Mejoró su desempeño.")
    elif nota2 == nota1:
        print("Mantuvo la nota.")
    else:
        print("Empeoró su desempeño.")
    
    if promedio >= 7:
        print("Promocionó la materia.")
    elif promedio >= 4:
        print("Debe rendir final.")
    else:
        print("Debe recursar la materia.")
    
    return promedio

nota1 = float(input("Ingrese la nota del primer examen: "))
nota2 = float(input("Ingrese la nota del segundo examen: "))

promedio = resultados_notas(nota1, nota2)
print(f"Promedio: {promedio}")
