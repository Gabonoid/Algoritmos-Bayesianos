class TipoClase:

    def __init__(self, datos):
        self.datos = datos
        self.total = len(datos)
        self.diccionario = self.generar_diccionario(self.datos)
        self.frecuencias = self.diccionario_frecuencias()

    def diccionario_frecuencias(self):
        frecuencias = []
        for dic in self.diccionario:
            diccionario = dic.copy()
            for clave, valor in diccionario.items():
                diccionario[clave] = valor / self.total
            frecuencias.append(diccionario)
        return frecuencias
    
    def get_columna_diccionario(self, indice):
        return self.diccionario[indice]
    
    def get_columna_frecuencia(self, indice):
        return self.frecuencias[indice]

    @staticmethod
    def separar_clases(data, indice, valor_clase):
        claseA = []
        claseB = []
        for sublista in data:
            clase = sublista.pop(indice)
            if clase == valor_clase:
                claseA.append(sublista)
            else:
                claseB.append(sublista)

        claseA = TipoClase(claseA)
        claseB = TipoClase(claseB)
        return claseA, claseB

    def generar_diccionario(self, lista):
        diccionario_clase = []
        for i, columna in enumerate(zip(*lista)):
            diccionario_columna = {}
            for valor in columna:
                if valor in diccionario_columna:
                    diccionario_columna[valor] += 1
                else:
                    diccionario_columna[valor] = 1
            diccionario_clase.append(diccionario_columna)
        return diccionario_clase
