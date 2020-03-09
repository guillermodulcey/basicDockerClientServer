class Process():
    def __init__(self, servers, parametros, espera):
        super().__init__()
        self.servers = servers
        self.parametros = parametros
        if espera == '':
            espera = 1
        else:
            self.espera = int(espera)

    def process(self, data):
        return 'empty'