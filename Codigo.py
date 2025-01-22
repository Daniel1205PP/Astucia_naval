def registrar_usuario():
    print("=== Registro de Usuario ===")

    # Pedir los datos del usuario
    nombre = input("Nombre: ")
    correo = input("Correo: ")
    contrasena = input("Contraseña: ")

    # Guardar los datos en un archivo de texto
    with open("usuarios.txt", "a") as archivo:
        archivo.write(f"{nombre},{correo},{contrasena}\n")

    print("\nUsuario registrado con éxito.")

def elegir_modo_juego():
    print("\n=== Selección de Modo de Juego ===")
    print("1. Individual")
    print("2. Dos Jugadores")

    while True:
        opcion = input("Elige una opción (1 o 2): ")
        if opcion == "1":
            print("Has elegido el modo de juego individual.")
            break
        elif opcion == "2":
            print("Has elegido el modo de juego para dos jugadores.")
            break
        else:
            print("Opción no válida. Por favor, elige 1 o 2.")

# Ejecutar las funciones
registrar_usuario()
elegir_modo_juego()

print("Los usuarios registrados se guardan en el archivo 'usuarios.txt'.")