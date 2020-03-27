class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://ivan:1111@localhost/fblog'
    CKEDITOR_PKG_TYPE = 'full'
    CKEDITOR_FILE_UPLOADER = 'upload'
    SECRET_KEY = 'dev key'
    CKEDITOR_ENABLE_CSRF = True
    CKEDITOR_LANGUAGE = 'uk'
    CKEDITOR_HEIGHT = '500'
    #POOL_PRE_PING = True
