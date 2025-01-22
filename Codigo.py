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

# Ejecutar la función de registro
registrar_usuario()

print("Los usuarios registrados se guardan en el archivo 'usuarios.txt'.")