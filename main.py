import pandas as pd
from bayes import *
from MatrizConfusion import *

# Primera parte
print('Primera Parte'.center(50, '-'))
# Lectura de datos
path = r'data\mushroom\agaricus-lepiota.csv'
# path = r'test.csv'
data = pd.read_csv(path, header=None).values.tolist()

# edible(comestible) = e
# poisonous (venenoso) = p
comestible, venenoso = TipoClase.separar_clases(data, 0, 'e')

# Propuesta Comestible (11)
test = ['x', 'y', 'y', 't', 'l', 'f', 'c', 'b', 'g', 'e',
                   'c', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p', 'n', 'n', 'g']

""" 
# Propuesta Venenoso (18)
test_venenoso = ['x', 's', 'n', 't', 'p', 'f', 'c', 'n', 'n', 'e',
              'e', 's', 's', 'w', 'w', 'p', 'w', 'o', 'p', 'k', 's', 'g',]
"""  
def porcentaje(clase_a, clase_b, total_num,frecuencia_a, frecencia_b):
    P = clase_a.total/total_num
    E = clase_b.total/total_num
    total = (P * frecuencia_a)/((P*frecuencia_a)+(E*frecencia_b))
    return total

def calcular_frec(clase, propuesta):
    sum_fac = 1
    for indice, valor in enumerate(propuesta):
            try:
                sum_fac *= clase.frecuencias[indice].get(valor)
            except:
                sum_fac = sum_fac
    return sum_fac
    
frecuencia_comestible = calcular_frec(comestible, test)
frecuencia_venenoso = calcular_frec(venenoso, test)

porcentaje_comestible = porcentaje(comestible, venenoso, len(data), frecuencia_comestible, frecuencia_venenoso)
porcentaje_venenoso = porcentaje(venenoso, comestible, len(data), frecuencia_venenoso, frecuencia_comestible)

print('Comestible con un', porcentaje_comestible*100, '%')
print('Venenoso con un', porcentaje_venenoso*100, '%')

# Segunda parte
print('Segunda Parte'.center(50, '-'))
# Generar pruebas
# Lectura de datos
path = r'data\mushroom\agaricus-lepiota.csv'
data = pd.read_csv(path, header=None).values.tolist()

entrenamiento, prueba = generar_pruebas(0.1, data, is_random=True)
comestible_entre, venenoso_entre = TipoClase.separar_clases(
    entrenamiento, 0, 'e')

matriz_binario = []
for entrada in prueba:
    esperado = 0 if entrada.pop(0) == 'e' else 1

    frecuencia_comestible = calcular_frec(comestible, entrada)
    frecuencia_venenoso = calcular_frec(venenoso, entrada)

    porcentaje_comestible = porcentaje(comestible, venenoso, len(data), frecuencia_comestible, frecuencia_venenoso)
    
    porcentaje_venenoso = porcentaje(venenoso, comestible, len(data), frecuencia_venenoso, frecuencia_comestible)
    
    prediccion = 1 if porcentaje_venenoso > porcentaje_comestible else 0
    matriz_binario.append([esperado, prediccion])


# Matriz Confusion
matrizConfusion = MatrizConfusion(matriz_binario)
print(matrizConfusion)
