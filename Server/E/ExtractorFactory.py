from E.ExtractorTraza import ExtractorTraza
from E.ExtractorGenerador import ExtractorGenerador

class ExtractorFactory():
    def __init__(self):
        pass

    def getExtractor(self, nombreExtractor, servers, parametros, espera):
        if nombreExtractor == "TRAZA":
            return ExtractorTraza(servers, parametros, espera)
        if nombreExtractor == "GENERADOR":
            return ExtractorGenerador(servers, parametros, espera)