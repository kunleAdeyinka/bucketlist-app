import os

# default configuration
class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = '3=\x0c\x84\x19R\xcfA\x0f\xaf!F\xacJ\xc1\x8f\xdd\x81,\x0b\x97R\x1b{'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    #print SQLALCHEMY_DATABASE_URI
    
    
class DevelopmentConfig(BaseConfig):
    DEBUG = True
    

class ProductionConfig(BaseConfig):
    DEBUG = False #to be absolutely sure that the debug mode is false
    