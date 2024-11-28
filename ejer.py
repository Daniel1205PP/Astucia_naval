# Definicion de variables (remplaza los valores con los que te proporciona)
V = 100  # numero de vacas
A = 200  # numero de aves
K = 5  # metros cuadrados de pasto por vaca
X = 10 # litros de leche por vaca por dia

# Problema 1: produccion de leche 
def produccion_leche(V, K, X):
    
    leche_por_dia = V * X
    leche_por_semana = leche_por_dia * 7
    return leche_por_semana

# Problema 2: produccion de huevos 
def produccion_huevos(A):
    
    gallinas_rapidas = A // 2
    gallinas_lentas = A - gallinas_rapidas
    
    huevos_rapidos_mes = gallinas_rapidas * (30 // 3)
    huevos_lentas_mes = gallinas_lentas * (30 // 5)
    
    huevos_totales = huevos_rapidos_mes + huevos_lentas_mes
    return huevos_totales

leche_semanal = produccion_leche(V, K, X)
huevos_mensuales = produccion_huevos(A)

print("Produccion de leche por semana :", leche_semanal,"litros")
print("Produccion de huevos en un mes :", huevos_mensuales,"huevos")
