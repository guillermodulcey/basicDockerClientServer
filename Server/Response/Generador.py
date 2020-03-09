import os
import threading

from Response.Response import Response

class Generador(Response):
    def __init__(self, name='client'):
        super().__init__(name)
        self.name = name

    def respond(self):
        return super().respond()

    def petition(self, message):
        valores = message.split(' ')

        os.system('gcc -o trace_generator/generator trace_generator/generator.c trace_generator/genericlib.c trace_generator/statlib.c -lm')
        xThread = threading.Thread(target=self.__saveData,args=(message,))
        xThread.start()

        self.message = f'{self.name}: Work accepted! {message}'

    def __saveData(self,valoresGenerador: str):
        result = os.popen(f'./trace_generator/generator {valoresGenerador}').read()
        nombre = valoresGenerador.split(' ')
        nombre = f'{nombre[0]} {nombre[2]} {nombre[5]}'
        nombre = nombre.replace(' ','_')
        f = open(f'trazas/{self.name}_{nombre}.txt','w')
        f.write(result)
        f.close()