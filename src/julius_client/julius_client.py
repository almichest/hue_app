import socket
from enum import Enum
import src.julius_client.julius_notification_parser as julius_parser

class JuliusClient(object):

    _host = "localhost"
    _port = 10500

    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def open(self):
        self.client.connect((self._host, self._port))

        while True:
            data = self.client.recv(4096).decode('utf-8')
            # dict = julius_parser.parse(data)
            print(data)


class JuliusClientReceiver:
    def on_receive(self, type, data):
        pass

class JuliusEventType(Enum):
    StartRec    = 1
    StartRecog  = 2
    EndRec      = 3
    EndRecog    = 4
    RecogOut    = 5
    Listen      = 6

client = JuliusClient()
client.open()
