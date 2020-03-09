from L.LoadTraza import LoadTraza
from L.LoadGenerador import LoadGenerador

class LoadFactory():
    def __init__(self):
        pass

    def getLoad(self, nombreLoad, servers, parametros, espera):
        if nombreLoad == "TRAZA":
            return LoadTraza(servers, parametros, espera)
        if nombreLoad == "GENERADOR":
            return LoadGenerador(servers, parametros, espera)