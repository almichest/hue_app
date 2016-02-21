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

        xml = '<ROOT>'
        while True:
            data = self.client.recv(4096).decode('utf-8')
            print('before data = ******************************')
            print(data)
            data = data.replace('.\n', '')
            data = data.replace('WORD="<s>"', '')
            print('after data = ******************************')
            print(data)
            if 0 <= data.find('<INPUT STATUS=\"STARTREC\"'):
                xml = '<ROOT>'

            xml += data
            if 0 <= data.find('<INPUT STATUS=\"LISTEN\"'):
                xml += '</ROOT>'
                print('xml = ******************************')
                print(xml)
                dic = julius_parser.parse(xml)
                print(dic)
                xml = ''


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
