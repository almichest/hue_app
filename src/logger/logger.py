__author__ = 'hira'
from datetime import datetime
import pytz

def log_with_time(text):
    now = datetime.now()
    now = pytz.utc.localize(now)
    now = now.astimezone(pytz.timezone('Asia/Tokyo'))
    now_str = now.strftime("%H:%M:%S")
    print(text + ' at ' + now_str)
