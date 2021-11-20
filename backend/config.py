import os

class Config(object):
    SECRET_KEY = os.urandom(32)
# Need make normal key