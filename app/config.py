import os
import secrets

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """
    Common configurations
    """
    TESTING = False
    DEBUG = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'andela')


class TestingConfig(Config):
    """
    Configurations for Testing, with a separate test database.
    """
    ENV = 'testing'
    DATABASE = 'test_epic'
    TESTING = True
    DEBUG = True


class DevelopmentConfig(Config):
    """
    Development configurations
    """
    ENV = 'development'
    DATABASE = 'epic'
    DEBUG = True
    TESTING = False


class ProductionConfig(Config):
    """
    Production configurations
    """
    ENV = 'production'
    DEBUG = False
    TESTING = False
    HOST = ''
    DATABASE = ''
    USER = ''
    PASSWORD = ''
    DEBUG = False
    TESTING = False

env_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}