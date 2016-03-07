from hue.hue_client import HueAPIClient
from julius_client.julius_client import JuliusClient
from julius_client.julius_client import JuliusClientListener
import logger.logger as logger

from enum import Enum
class HueControllerState(Enum):
    normal  = 0
    waiting_light = 1

class HueController(JuliusClientListener):

    def __init__(self):
        self.julius_client = JuliusClient()
        self.julius_client.listener = self
        self.hue_client = HueAPIClient()

    def open(self):
        self.hue_client.find_bridge()
        self.hue_client.connect()
        self.state = HueControllerState.normal
        self.julius_client.open()

    __denki = 'でんき'
    __on_words = ['つけて']
    __off_words = ['けして']
    def on_receive(self, data):
        try:
            root = data['ROOT']
            recogout = root['RECOGOUT']
            shypo = recogout['SHYPO']
            whypo = shypo['WHYPO']
            for dic in whypo:
                if '@WORD' in dic:
                    word = dic['@WORD']
                    logger.log_with_time('Received ' + word)
                    self._update_state(word)

        except:
            print('ERROR Getting parameter from data: ')
            print(data)

    def _update_state(self, word):
        try:
            if self.state == HueControllerState.normal:
                if word == self.__denki:
                    self.state = HueControllerState.waiting_light
                else :
                    self.state = HueControllerState.normal
            elif self.state == HueControllerState.waiting_light:
                if word in self.__on_words:
                    self.hue_client.on()
                elif word in self.__off_words:
                    self.hue_client.off()
                self.state = HueControllerState.normal
        except ValueError:
            print('Error : ' + ValueError)


