# 1. Desarrollar un programa que determine si en una lista no existen elementos repetidos

def no_hay_repetiones(lista):
    return len(lista) == len(set(lista))

lista1 = [2, 3, 1, 4, 5]
print(no_hay_repetiones(lista1))

# 2. desarrollar un programa que determine si una lista se encuentran una cadena de caracteres con dos o mas vocales. si la cadena existe debe imprimirla y si no existe debe imprimir no existe 

def cadena_con_vocales(lista):
    vocales = "aeiouAEIOU"
    for elemento in lista:
        if isinstance(elemento, str):
            contador = sum(1 for letra in elemento if letra in vocales)
            if contador >= 2:
                return elemento
            return "no existe"
lista2 = ["aeiouAEIOU","hola","lunes","local"]
print(cadena_con_vocales(lista2))

# 3. DESARROLLA UN PROGRAMA QUE DADAS DOS LISTAS DETERMINE QUE ELEMENTOS TIENE LA PRIMERA LISTA QUE NO TENGA LA SEGUNDA LISTA   

lista3 = [1, 2, 3, 4, 5]
lista4 = [4, 5, 6, 7, 8]

def elementos_unicos(lista3, lista4):
    return list(set(lista3) - set(lista4))
resultado = elementos_unicos(lista3, lista4)
print("Los elementos en la primera fila que no existen en la segunda son ", resultado)

# 4. desarrolla un algoritmo que calcule el promedio de un arreglo de reales   

def calcular_promedio(arreglo):
    if not arreglo:
        return 0
    return sum(arreglo) / len(arreglo)

numeros = [4.5, 8.2, 5.6, 2.5]
promedio = calcular_promedio(numeros)
print("El promedio es ", promedio)

# 5. desarrola un algoritmo que determine la madiana de un arreglo de enteros. la madiana es el numero que queda en la mitad del arreglo despues de ser ordenado

def calcular_media(arreglo):
    if not arreglo:
        return None
    arreglo_ordenado = sorted(arreglo)
    n = len(arreglo_ordenado)
    medio = n // 2 
    if n % 2 == 1:
        return arreglo_ordenado[medio]
    else:
        return(arreglo_ordenado[medio - 1] + arreglo_ordenado[medio]) / 2

numeros = [3, 4, 7, 9]
mediana = calcular_media(numeros)
print("la mediana es", mediana)
