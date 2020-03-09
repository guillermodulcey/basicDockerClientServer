from T.TransformPromedio import TransformPromedio
from T.TransformGenerador import TransformGenerador

class TransformFactory():
    def __init__(self):
        pass

    def getTransform(self, nombreTransform, servers, parametros, espera):
        if nombreTransform == "TRAZA":
            return TransformPromedio(servers, parametros, espera)
        if nombreTransform == "GENERADOR":
            return TransformGenerador(servers, parametros, espera)