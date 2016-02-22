import socket
from enum import Enum
import src.julius_client.julius_notification_parser as julius_parser

class JuliusClient(object):

    _host = "localhost"
    _port = 10500

    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    @property
    def listener(self):
        return self.__listener

    @listener.setter
    def listener(self, value):
        self.__listener = value

    @listener.deleter
    def listener(self):
        del self.__listener


    def open(self):
        self.client.connect((self._host, self._port))

        xml = '<ROOT>'
        while True:
            data = self.client.recv(4096).decode('utf-8')
            data = data.replace('.\n', '')
            data = data.replace('WORD="<s>"', '')
            if 0 <= data.find('<INPUT STATUS=\"STARTREC\"'):
                xml = '<ROOT>'

            xml += data
            if 0 <= data.find('<INPUT STATUS=\"LISTEN\"'):
                xml += '</ROOT>'
                dic = julius_parser.parse(xml)
                self.listener.on_receive(dic)
                xml = ''


class JuliusClientListener(object):
    def on_receive(self, data):
        pass

