class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root@localhost/firstblog'
    CKEDITOR_PKG_TYPE = 'standart'
    CKEDITOR_SERVE_LOCAL = False
    CKEDITOR_FILE_UPLOADER = 'upload'
