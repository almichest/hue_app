from hue.hue_client import HueAPIClient
from julius_client.julius_client import JuliusClient
from julius_client.julius_client import JuliusClientListener

class HueController(JuliusClientListener):

    def __init__(self):
        self.julius_client = JuliusClient()
        self.julius_client.listener = self
        self.hue_client = HueAPIClient()

    def open(self):
        self.hue_client.find_bridge()
        self.hue_client.connect()
        self.julius_client.open()

    __light_on_words = ['おはよう', 'ただいま']
    __light_off_words = ['おやすみ', 'いってきます']
    def on_receive(self, data):
        try:
            print('on_receive')
            root = data['ROOT']
            recogout = root['RECOGOUT']
            shypo = recogout['SHYPO']
            print(shypo)
            whypo = shypo['WHYPO']
            print(whypo)
            for dic in whypo:
                if '@WORD' in dic:
                    word = dic['@WORD']
                    print('word = ' + word)
                    if word in self.__light_on_words:
                        self.hue_client.on()
                    elif word in self.__light_off_words:
                        self.hue_client.off()

        except:
            print('ERROR Getting parameter from data: ')
            print(data)


