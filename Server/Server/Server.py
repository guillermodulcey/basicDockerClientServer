import socket
import select
import sys
import pickle

from Response.Response import Response

class Server():
    def __init__(self, port, response: Response, header_length = 10, enco = 'utf-8', ip='host'):
        super().__init__()
        self.HEADER_LENGTH = header_length
        self.enco = enco
        self.port = port
        self.response = response

        if ip == 'host':
            hostname = socket.gethostname()
            self.ip = socket.gethostbyname(hostname)
        else:
            self.ip = '127.0.0.1'

    def launch_server(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.ip,self.port))
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        print(self.ip)

        server_socket.listen()

        sockets_list = [server_socket]

        clients = {}

        while True:
            read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)
            for notified_socket in read_sockets:
                if notified_socket == server_socket:
                    client_socket, client_address = server_socket.accept()

                    sockets_list.append(client_socket)

                    clients[client_socket] = client_address
                    print(f"Connection from {client_address} has been established!")

                else:
                    message = self.__receive_message(notified_socket)
                    if message is False:
                        print(f"Closed connection from {clients[notified_socket]}")
                        sockets_list.remove(notified_socket)
                        del clients[notified_socket]
                        continue
                    print(f"Received message: {message['header']} -- {message['data'].decode(self.enco)}")

                    for client_socket in clients:
                        if client_socket == notified_socket:
                            response = self.__respond_message(message['data'].decode(self.enco))
                            response_header = f"{len(response):< {self.HEADER_LENGTH}}".encode(self.enco)
                            client_socket.send(response_header + response)

            for notified_socket in exception_sockets:
                sockets_list.remove(notified_socket)
                del clients[notified_socket]

    def __receive_message(self, client_socket):
        try:
            message_header = client_socket.recv(self.HEADER_LENGTH)
            if not len(message_header):
                return False
            message_length = int(message_header.decode(self.enco).strip())
            return {"header": message_length, "data": client_socket.recv(message_length)}
        except:
            return False

    def __respond_message(self, message):
        self.response.petition(message)
        return pickle.dumps(self.response)