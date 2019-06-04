import random
import string
import datetime
from datetime import date


def generate_order_id():
    date_str = date.today().strftime('%Y%m%d')
    rand_str = ''.join([random.choice(string.digits) for count in range(3)])
    return date_str + rand_str
