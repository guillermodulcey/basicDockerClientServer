import os

from E.Extractor import Extractor

class ExtractorGenerador(Extractor):
    def __init__(self, servers, parametros, espera):
        super().__init__(servers, parametros, espera)

    def process(self, folder):
        archivos = os.listdir(folder)
        for archivo in archivos:
            if archivo == '.DS_Store':
                continue
            resultado = self.__obtenerParametros(f'{folder}/{archivo}')
        return resultado

    ## Métodos auxiliares

    def __obtenerParametros(self,file):
        f = open(file,'r')
        valores = f.read().split('\n')
        f.close()
        return valores