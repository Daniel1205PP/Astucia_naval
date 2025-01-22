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

def iniciar_sesion():
    print("\n=== Inicio de Sesión ===")

    correo = input("Correo: ")
    contrasena = input("Contraseña: ")

    with open("usuarios.txt", "r") as archivo:
        usuarios = archivo.readlines()
        for usuario in usuarios:
            datos = usuario.strip().split(",")
            if correo == datos[1] and contrasena == datos[2]:
                print(f"\nInicio de sesión exitoso. Bienvenido, {datos[0]}!")
                return True

    print("\nCorreo o contraseña incorrectos.")
    return False

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

# Flujo del programa
print("Bienvenido al sistema.")
accion = input("¿Quieres registrarte (R) o iniciar sesión (I)? ").strip().upper()

if accion == "R":
    registrar_usuario()
elif accion == "I":
    if iniciar_sesion():
        elegir_modo_juego()
else:
    print("Opción no válida. Saliendo del programa.")

print("Los usuarios registrados se guardan en el archivo 'usuarios.txt'.")