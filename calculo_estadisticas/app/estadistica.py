from numpy import mean, std

class Interno:
    def __init__(self, data):
        """
        Metodo que guarda el promedio y la desviacion estandar de un arreglo
        """
        self.promedio = mean(data)
        self.desviacion = std(data)

class Datos:
    def __init__(self, magpsf_corr, sigmapsf_corr):
        """
        Metodo que inicializa una estadistica, se pide el arreglo
        que contiene todos los magpsf corregidos y los sigmapsf corregidos
        """
        self.magpsf_corregidos = Interno(magpsf_corr).__dict__
        self.sigmapsf_corr = Interno(sigmapsf_corr).__dict__

class Estadistica:
    def __init__(self, green, red):
        """
        Metodo que calula las estadisticas de los datos ingresados
        """
        self.verde = Datos(green.get('magpsf_corr'), green.get('sigmapsf_corr')).__dict__
        self.rojo = Datos(red.get('magpsf_corr'), red.get('sigmapsf_corr')).__dict__
