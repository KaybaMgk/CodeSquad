def listarLeyes(leyes):
    print("\nLeyes: \n")
    contador = 1
    for ley in leyes:
        datos = "{0}. Registro: {1} | Tipo de normativa: {2} | Numero normativa: {3} | Fecha: {4} | Descripcion: {5} | Categoria: {6} | Jurisdiccion: {7} | Organo legislativo: {8}"
        print(
            datos.format(
                contador,
                ley[0],
                ley[1],
                ley[2],
                ley[3],
                ley[4],
                ley[5],
                ley[6],
                ley[7],
                ley[8],
            )
        )
        contador = contador + 1
    print(" ")


def pedirDatosRegistro():
    leyCorrecta = False
    while not leyCorrecta:
        ley = input("Ingrese ley: ")
        if len(ley) >= 4:
            leyCorrecta = True
        else:
            print("Número incorrecto, debería contener al menos 4 números.")

    fecha = input("Ingrese la fecha de declaración: ")
    descripcion = input("Ingrese descripción: ")
    categoria = input(
        "Indique si la ley pertenece a la categoría laboral o derecho informático: "
    )
    jurisdiccion = input("Indique si la jurisdicción es nacional o provincial: ")
    or_lesgislativo = input("Ingrese el órgano legislativo: ")
    palabra_clave = input("Ingrese palabras claves que compongan la ley: ")

    ley = (fecha, descripcion, categoria, jurisdiccion, or_lesgislativo, palabra_clave)
    return ley


def pedirDatosActualizacion(leyes):
    listarLeyes(leyes)
    existeLey = False
    leyEditar = input("Ingrese el número de ley a editar: ")
    for ley in leyes:
        if ley[0] == leyEditar:
            existeLey = True
            break

    if existeLey:
        descripcion = input("Ingrese descripción a modificar: ")

        fechaModificacionLey = False
        while not fechaModificacionLey:
            fecha = input("Ingrese la fecha de modificación de la legislación: ")
            if fecha.isnumeric():
                if (fecha) > 0:
                    fechaModificacionLey = True
                    fecha = int(fecha)
                else:
                    print("La fecha ingresada no es válida.")
            else:
                print("La fecha ingresada no es válida.")

        ley = (leyEditar, descripcion, fecha)
    else:
        ley = None

    return ley


def pedirDatosEliminacion(ley):
    listarLeyes(ley)
    existeLey = False
    leyEliminar = input("Ingrese el número de ley a eliminar: ")
    for ley in ley:
        if ley[0] == leyEliminar:
            existeLey = True
            break

    if not existeLey:
        leyEliminar = ""

    return leyEliminar
