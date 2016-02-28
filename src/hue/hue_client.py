__author__ = 'hira'

from phue import Bridge


class HueAPIClient(object):

    def __init__(self):
        pass

    def find_bridge(self):
        import hue.bridge_scanner as bridge_scanner

        while True:
            self.ip = bridge_scanner.get_bridge_ips()[0]
            if 0 < len(self.ip):
                break

        print('Bridge found ' + self.ip)
        self.bridge = Bridge(self.ip)

    def connect(self):
        self.bridge.connect()

    def on(self):
        lights = self.bridge.get_light_objects()

        for light in lights:
            light.on = True

    def off(self):
        lights = self.bridge.get_light_objects()

        for light in lights:
            light.on = False
