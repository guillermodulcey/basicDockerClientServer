class Response():
    def __init__(self,name='client'):
        super().__init__()
        self.name = name

    def respond(self):
        return self.message
    
    def petition(self, message = 'Hi'):
        self.message = message