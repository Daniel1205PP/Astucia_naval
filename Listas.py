def no_hay_repetidos(lista):
    return len(lista) == len(set(lista))

def cadena_palindroma(lista):
    for elemento in lista:
        if isinstance(elemento, str) and elemento == elemento[::-1]:
            return elemento
    return "No existe"

def cadena_con_vocales(lista):
    vocales = "aeiouAEIOU"
    for elemento in lista:
        if isinstance(elemento, str):
            contador = sum(1 for letra in elemento if letra in vocales)
            if contador >= 2:
                return elemento
    return "No existe"

def lista_palindroma(lista):
    return lista == lista[::-1]

# Ejemplo de uso
lista1 = [1, 2, 3, 4, 5]
lista2 = ["oso", "perro", "radar", "casa"]
lista3 = ["hola", "aeiou", "python", "code"]
lista4 = [1, 2, 3, 2, 1]

print(no_hay_repetidos(lista1))  # True
print(cadena_palindroma(lista2))  # "oso" (o "radar")
print(cadena_con_vocales(lista3))  # "aeiou"
print(lista_palindroma(lista4))  # True
