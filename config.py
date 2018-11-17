import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    ##国际化
    BABEL_DEFAULT_LOCALE = 'zh_CN'
    ##自动提交数据库orm
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    ##邮件设置
    MAIL_SERVER = "smtp.asppj.top"
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME") or "lsp@asppj.top"
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD") or ""
    FLASK_MAIL_SUBJECT_PREFIX = "图谱展示"
    FLASK_MAIL_SENDER = "图谱管理员<lsp@asppj.top>"
    MAIL_DEFAULT_SENDER = "图谱管理员<lsp@asppj.top>"
    ##管理员邮箱
    FLASK_ADMIN = "lsp@asppj.top"
    ##上传
    UPLOADS_DEFAULT_DEST = os.path.join(basedir, "main/upload/").replace("/", "\\")
    UPLOADS_DEFAULT_URL = "localhost:5000"

    UPLOADS_HEADIMG_DEST = os.path.join(basedir, "main/upload/HEADIMG").replace("/", "\\")
    UPLOADS_HEADIMG_URL = "localhost:5000"
    FLASK_POSTS_PAGE = 16
    CKEDITOR_SERVE_LOCAL = True
    CKEDITOR_PKG_TYPE = "basic"
    filebrowserUploadUrl = "/upload/ckeditor/"
    ##mongo
    MONGO_URI = "mongodb://server.asppj.top:27017/zhilian"
    MONGO_HOST = "106.12.207.35"
    MONGO_PORT = 27017
    MONGO_USERNAME = "zhilian_db"
    MONGO_PASSWORD = "zhilian_db123"


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG_TB_TEMPLATE_EDITOR_ENABLED = True
    DEBUG_TB_PROFILER_ENABLED = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False


class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = True


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'prodection': ProductionConfig,
    'default': DevelopmentConfig
}
