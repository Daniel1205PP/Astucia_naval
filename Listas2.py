# 1. Escriba un programa que tome una lista de números enteros como entrada y determine el
#valor máximo de la lista. Si hay varios valores máximos, el programa debe imprimir el primero que encuentre.

# 2. Escriba un programa que tome una lista de cadenas y una cadena de destino como entrada. El programa debe determinar si la cadena de destino existe en la lista. Si existe, el programa debe imprimir su índice. De lo contrario, debe imprimir "No encontrado"

# 3.  Escriba un programa que tome una lista de números (enteros o de punto flotante) como entrada y calcule el promedio de los números de la lista. El programa debe imprimir el promedio con dos decimales.

# 4.  Escriba un programa que tome una lista de caracteres como entrada y cuente la cantidad de ocurrencias de un carácter específico en la lista. El programa debe imprimir la cantidad de ocurrencias.

def encontrar_maximo(lista):
    if not lista:
        return "La lista está vacía."
    
    maximo = lista[0]  # Asignamos el primer elemento como máximo inicial
    
    for num in lista:
        if num > maximo:
            maximo = num
    
    return maximo

def buscar_cadena(lista, objetivo):
    if objetivo in lista:
        return lista.index(objetivo)
    return "No encontrado"

def calcular_promedio(lista):
    if not lista:
        return "La lista está vacía."
    
    promedio = sum(lista) / len(lista)
    return f"{promedio:.2f}"

def contar_ocurrencias(lista, caracter):
    return lista.count(caracter)


numeros = list(map(float, input("Ingrese una lista de números separados por espacios: ").split()))
resultado = encontrar_maximo(numeros)
print("El valor máximo encontrado es:", resultado)

resultado_promedio = calcular_promedio(numeros)
print("El promedio de los números es:", resultado_promedio)

cadenas = input("Ingrese una lista de cadenas separadas por espacios: ").split()
objetivo = input("Ingrese la cadena de destino: ")
resultado_busqueda = buscar_cadena(cadenas, objetivo)
print("Índice de la cadena encontrada:", resultado_busqueda)

caracteres = list(input("Ingrese una lista de caracteres sin espacios: "))
caracter_objetivo = input("Ingrese el carácter a contar: ")
ocurrencias = contar_ocurrencias(caracteres, caracter_objetivo)
print("Cantidad de ocurrencias del carácter:", ocurrencias)
