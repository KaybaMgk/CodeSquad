# importamos la conexion a la base de datos
from conexion import db_leyes

# importamos las funciones necesarias para el CRUD
from conexion import funciones

# definimos el menu principal con las opciones del CRUD y la opcion de salir del sistema


def menuPrincipal():
    continuar = True
    while (continuar):
        opcionCorrecta = False
        while (not opcionCorrecta):
            print("==================== MENÚ PRINCIPAL ====================")
            print("1.- Listar leyes")
            print("2.- Registrar ley")
            print("3.- Actualizar ley")
            print("4.- Eliminar ley")
            print("5.- Salir")
            print("========================================================")
            opcion = int(input("Seleccione una opción: "))

            if opcion < 1 or opcion > 5:
                print("Opción incorrecta, ingrese nuevamente")
            elif opcion == 5:
                continuar = False
                print("¡Gracias por usar este sistema!")
                break
            else:
                opcionCorrecta = True
                ejecutarOpcion(opcion)

# definimos el comportamiento segun la opcion elegida


def ejecutarOpcion(opcion):
    bdlegislatura = db_leyes()
# opcion R del CRUD: READ(leer)
    if opcion == 1:
        try:
            leyes = bdlegislatura.listarLeyes()
            if len(leyes) > 0:
                funciones.listarLeyes(leyes)
            else:
                print("No se encontraron leyes")
        except:
            print("Ocurrió un error")
# opcion C del CRUD: CREATE(crear)
    elif opcion == 2:
        ley = funciones.pedirDatosLey()
        try:
            bdlegislatura.registrarLey(ley)
        except:
            print("Ocurrió un error")
# opcion U del CRUD: UPDATE(modificar)
    elif opcion == 3:
        try:
            ley = bdlegislatura.listarLeyes()
            if len(ley) > 0:
                ley = funciones.pedirDatosActualizacion(ley)
                if ley:
                    bdlegislatura.actualizarLey(ley)
                else:
                    print("Número de ley a actualizar no encontrado\n")
            else:
                print("No se encontró la ley")
        except:
            print("Ocurrió un error")
# opcion D del CRUD: DELETE(eliminar)
    elif opcion == 4:
        try:
            ley = bdlegislatura.listarLeyes()
            if len(ley) > 0:
                numeroEliminar = funciones.pedirDatosEliminacion(ley)
                if not (numeroEliminar == ""):
                    bdlegislatura.eliminarLey(numeroEliminar)
                else:
                    print("Número de ley no encontrado\n")
            else:
                print("No se encontró la ley")
        except:
            print("Ocurrió un error")
    else:
        print("Opción no válida")


menuPrincipal()