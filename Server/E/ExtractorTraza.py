import os

from E.Extractor import Extractor
from statistics import mean

class ExtractorTraza(Extractor):
    def __init__(self, servers, parametros, espera):
        super().__init__(servers, parametros, espera)

    def process(self, folder):
        numTrabajadores = int(self.parametros[0])
        promedios = []
        archivos = os.listdir(folder)
        for archivo in archivos:
            if archivo == '.DS_Store':
                continue
            tiempos  = self.__obtenerTiempos(f'{folder}/{archivo}')
            tiemposTrabajador = self.__repartirTiempos(tiempos,numTrabajadores)
            promediosTrabajador = self.__obtenerPromedios(tiemposTrabajador)
            promedios.append(promediosTrabajador)
        return promedios

    ## Métodos auxiliares

    def __obtenerTiempos(self,file):
        tiempos = []
        f = open(file,'r')
        for x in f:
            valores = x.split(' ')
            tiempos.append(float(valores[0]))
        f.close()
        return tiempos

    def __repartirTiempos(self, tiempos, numTrabajadores):
        trabajadores = []
        for i in range(numTrabajadores):
            trabajadores.append([])
        for i in range(len(tiempos)):
            trabajadores[i%numTrabajadores].append(tiempos[i])
        return trabajadores

    def __obtenerPromedios(self, trabajadores):
        promedios = []
        for trabajador in trabajadores:
            tiempos = self.__obtenerTiemposTrabajador(trabajador)
            promedio = mean(tiempos)
            promedios.append(promedio)
        return promedios

    def __obtenerTiemposTrabajador(self, trabajador):
        anterior = 0
        tiempos = []
        for x in trabajador:
            tiempos.append(x-anterior)
            anterior = x
        return tiempos