__author__ = 'hira'
from src.hue.hue_client import HueAPIClient

client = HueAPIClient()

client.find_bridge()

client.connect()

client.random()