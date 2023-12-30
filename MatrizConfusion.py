import random


class MatrizConfusion:

    def __init__(self, matriz):
        self.matriz = matriz
        self.vp, self.vn, self.fp, self.fn = self.contador()
        self.A = self.exactitud(self.vp, self.vn, self.fp, self.fn)
        self.R = self.sensibilidad(self.vp, self.fn)
        self.P = self.precision(self.vp, self.fp)
        self.TNR = self.razon_verdaderos_negativos(self.vn, self.fp)
        self.FPR = self.razon_falsos_positivos(self.fp, self.vn)
        self.RNR = self.razon_falsos_negativos(self.fn, self.vp)

    def __repr__(self):
        return f"Verdaderos Positivos: {self.vp}\nVerdaderos Negativos: {self.vn}\nFalsos Positivos: {self.fp}\nFalsos Negativos: {self.fn}\nExactitud: {self.A}\nPrecision: {self.P}\nSensibilidad: {self.R}\nTNR: {self.TNR}\nFPR: {self.FPR}\nRNR: {self.RNR}\nLa función de clasificación tuvo un {round(self.A*100, 2)}% de exactitud por lo que un {'buen' if self.A > 0.85 else 'mal'} clasificador."

    def contador(self):
        vp = vn = fp = fn = 0
        for linea in self.matriz:
            if linea[0] == 1 and linea[1] == 1:
                vp += 1
            elif linea[0] == 1 and linea[1] == 0:
                fn += 1
            elif linea[0] == 0 and linea[1] == 1:
                fp += 1
            elif linea[0] == 0 and linea[1] == 0:
                vn += 1
        return vp, vn, fp, fn

    @staticmethod
    def exactitud(vp, vn, fp, fn):
        try:
            return (vp + vn) / (vp + vn + fp + fn)
        except:
            return 0

    @staticmethod
    def sensibilidad(vp, fn):
        try:
            return vp / (vp + fn)
        except:
            return 0

    @staticmethod
    def precision(vp, fp):
        try:
            return vp / (vp + fp)
        except:
            return 0

    @staticmethod
    def razon_verdaderos_negativos(vn, fp):
        try:
            return vn / (vn + fp)
        except:
            return 0

    @staticmethod
    def razon_falsos_positivos(fp, vn):
        try:
            return fp / (fp + vn)
        except:
            return 0

    @staticmethod
    def razon_falsos_negativos(fn, vp):
        try:
            return fn / (fn + vp)
        except:
            return 0


def generar_pruebas(porcentaje, datos, guardar=False, is_random=False):
    porcentaje_promedio = int(len(datos) * porcentaje)

    if is_random:
        prueba = random.sample(datos, porcentaje_promedio)
        entrenamiento = [dato for dato in datos if dato not in prueba]
    else:
        prueba = datos[:porcentaje_promedio]
        entrenamiento = datos[porcentaje_promedio:]

    if guardar:
        import pandas as pd
        pd.DataFrame(prueba).to_csv(
            "data/prueba.csv", index=False, header=False)
        pd.DataFrame(entrenamiento).to_csv(
            "data/entrenamiento.csv", index=False, header=False)

    return entrenamiento, prueba
