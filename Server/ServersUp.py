import sys
import os
import socket
import threading
import time

from Response.Simulador import Simulador

class ServerUp():
    def __init__(self,trabajadores,puerto_inicial,tipo,ip='127.0.0.1'):
        super().__init__()
        self.ip = ip
        self.trabajadores = trabajadores
        self.puerto_inicial = puerto_inicial
        self.tipo = tipo

    def initialize(self):
        for i in range(self.trabajadores):
            os.system(f'docker run -tid --name {self.tipo}{i} -p {self.puerto_inicial+i}:{self.puerto_inicial+i} -v /Users/cinvestav-UT/Documents/Distribuidos/Server:/home/simulator pyc')

    def run(self):
        servers = []
        for i in range(self.trabajadores):
            xThread = threading.Thread(target=self.__up,args=(i,))
            xThread.start()
            servers.append(f'{self.ip}:{self.puerto_inicial+i}')

        lista = ' '
        lista = lista.join(servers).replace(' ',';')
        print(lista)

    def kill(self):
        for i in range(self.trabajadores):
            xThread = threading.Thread(target=self.__down,args=(i,))
            xThread.start()

    def __up(self,i):
        os.system(f'docker exec -tid {self.tipo}{i} python3 ServerUp.py {self.puerto_inicial+i} {self.tipo}')

    def __down(self,i):
        os.system(f'docker rm -f {self.tipo}{i}')


trabajadores = int(sys.argv[1])
PORT = int(sys.argv[2])
tipo = sys.argv[3]
command = sys.argv[4]


SU = ServerUp(trabajadores,PORT,tipo)

if command == 'run':
    SU.initialize()
    SU.run()
else:
    SU.kill()