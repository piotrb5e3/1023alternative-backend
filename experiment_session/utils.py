import random
import string
import re

chars = string.ascii_letters + string.digits
chars = re.sub('[1liIoO0]', '', chars)


def random_alphanumeric(length):
    return ''.join([random.choice(chars) for i in range(length)])
