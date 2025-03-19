from logging import config
import os


basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    pass


class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    pass


class TestingConfig(Config):
    pass


    TESTING = True
