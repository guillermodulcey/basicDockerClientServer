import os
import threading

from Response.Response import Response

class Simulador(Response):
    def __init__(self, name='client'):
        super().__init__(name)
        self.name = name

    def respond(self):
        return super().respond()

    def petition(self, message):
        valores = message.split(' ')

        promedio = valores[0]
        servicio = valores[1]
        delays = valores[2]

        os.system('gcc -o queuesimulator/single queuesimulator/single.c -lm')
        valoresSimulador = f'{promedio} {servicio} {delays}'
        xThread = threading.Thread(target=self.__saveData,args=(valoresSimulador,))
        xThread.start()

        self.message = f'{self.name}: Work accepted! {valoresSimulador}'

    def __saveData(self,valoresSimulador: str):
        result = os.popen(f'./queuesimulator/single {valoresSimulador}').read()
        nombre = valoresSimulador.replace(' ','_')
        f = open(f'results/{self.name}_{nombre}.txt','w')
        f.write(result)
        f.close()