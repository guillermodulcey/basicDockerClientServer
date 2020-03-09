import os
import time

from L.Load import Load

class LoadGenerador(Load):
    def __init__(self, servers, parametros, espera):
        super().__init__(servers, parametros, espera)

    def process(self,folder):
        partes = int(self.parametros[0])
        result = []
        archivos = os.listdir(folder)
        contador = 0
        while(True):
            archivos = os.listdir(folder)
            if len(archivos) < (partes+1) and contador < self.espera:
                time.sleep(1)
                contador += 1
            else:
                break
        for archivo in archivos:
            if archivo == '.DS_Store':
                continue
            f = open(f'{folder}/{archivo}','r')
            metricas = f.read().split('\n')
            metricas.remove('')
            result.append(metricas)
            f.close()
        return result