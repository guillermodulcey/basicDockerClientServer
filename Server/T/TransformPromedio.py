import os
from Client.Client import Client

from T.Transform import Transform
from Response.Simulador import Simulador

class TransformPromedio(Transform):
    def __init__(self,servers, parametros, espera):
        super().__init__(servers, parametros, espera)

    def process(self, arreglo):
        results = []
        if self.servers == ['']:
            for parte in arreglo:
                for i in range(len(parte)):
                    results.append(Simulador().petition(f'{parte[i]} {self.parametros[0]} {self.parametros[1]}'))
        else:
            for parte in arreglo:
                for i in range(len(parte)):
                    direccion = self.servers[i%len(self.servers)].split(':')
                    results.append(Client(direccion[0],int(direccion[1])).launch_client(f'{parte[i]} {self.parametros[0]} {self.parametros[1]}'))
        return results
