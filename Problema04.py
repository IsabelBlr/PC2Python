def ingresar_calificaciones(num_alumnos):
    lista_alumnos = []  

    for i in range(num_alumnos):
        alumno = input("Ingrese el nombre del alumno: ")
        notas = []  

        for j in range(3):
            nota = float(input(f"Ingrese la calificación {j+1} del alumno {alumno}: "))
            notas.append(nota)

        lista_alumnos.append({"Alumno": alumno, "Notas": notas})

    return lista_alumnos

def mostrar_listado_alumnos(lista_alumnos):
    print("Listado de alumnos:")
    for alumno in lista_alumnos:
        print(f"Alumno: {alumno['Alumno']}, Notas: {alumno['Notas']}")

num_alumnos = int(input("Ingrese el número de alumnos: "))

lista_alumnos = ingresar_calificaciones(num_alumnos)

mostrar_listado_alumnos(lista_alumnos)