import sys
import socket

from Server.Server import Server
from Response.Simulador import Simulador
from Response.Generador import Generador

PORT = int(sys.argv[1])
response = sys.argv[2]

hostname = socket.gethostname()
hostname = socket.gethostbyname(hostname)

if response == 'simulador':
    Server(PORT,Simulador(f'{hostname}:{PORT}'),ip='host').launch_server()
if response == 'generador':
    Server(PORT,Generador(f'{hostname}:{PORT}'),ip='host').launch_server()