class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://ivan:1111@localhost/fblog'
    #CKEDITOR_PKG_TYPE = 'standart'
    CKEDITOR_SERVE_LOCAL = False
    CKEDITOR_FILE_UPLOADER = 'upload'
    SECRET_KEY = 'dev key'
    CKEDITOR_ENABLE_CSRF = True
