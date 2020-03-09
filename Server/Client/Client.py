import socket
import sys
import pickle

from Response.Response import Response

class Client():
    def __init__(self, ip, port, header_length = 10, enco = 'utf-8'):
        super().__init__()
        self.HEADER_LENGTH = header_length
        self.ip = ip
        self.port = port
        self.enco = enco

    def launch_client(self, message):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((self.ip, self.port))

        if message:
            message = message.encode(self.enco)
            message_header = f"{len(message):< {self.HEADER_LENGTH}}".encode(self.enco)
            client_socket.send(message_header + message)

        try:
            message_header = client_socket.recv(self.HEADER_LENGTH)
            if not len(message_header):
                    print("connection closed by the server")
                    sys.exit()
            message_length = int(message_header.decode(self.enco).strip())
            message = client_socket.recv(message_length)
            message = pickle.loads(message)
            return message.respond()
        except Exception as e:
            print('General error:', str(e))
            sys.exit()

