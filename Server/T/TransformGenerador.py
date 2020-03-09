import os
from Client.Client import Client

from T.Transform import Transform
from Response.Generador import Generador

class TransformGenerador(Transform):
    def __init__(self,servers, parametros, espera):
        super().__init__(servers, parametros, espera)

    def process(self, arreglo):
        results = []
        if self.servers == ['']:
            for parte in arreglo:
                results.append(Generador().petition(f'{parte}'))
        else:
            contador = 0
            for parte in arreglo:
                direccion = self.servers[contador%len(self.servers)].split(':')
                results.append(Client(direccion[0],int(direccion[1])).launch_client(f'{parte}'))
                contador += 1
        return True