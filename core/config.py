import os

class BaseConfig:
    DATABASE_URI = 'sqlite:///./store.sqlite3'
    ECHO_QUERIES = False
    TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'fallback-secret-key')

class DevConfig(BaseConfig):
    DEBUG_MODE = True

class ProdConfig(BaseConfig):
    DEBUG_MODE = False

configurations = {
    'development': DevConfig,
    'production': ProdConfig
}
