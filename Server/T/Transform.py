from Process.Process import Process

class Transform(Process):
    def __init__(self, servers, parametros, espera):
        super().__init__(servers, parametros, espera)

    def process(self, data):
        return 'empty'