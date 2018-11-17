from flask import Flask
from flask_login import LoginManager
# from flask_pymongo import PyMongo
from flask_sqlalchemy import SQLAlchemy

from config import config
from src.regist_app import regist_app
from .mail import mail

sql_db = SQLAlchemy()
login_manager = LoginManager()

def create_all(config_name):
    ##初始化app
    app = Flask(__name__)
    ##导入配置文件
    app.config.from_object(config[config_name])
    # ##数据库
    # sql_db.init_app(app)
    # mongo_db.init_app(app)
    # ##界面ui
    # Bootstrap(app)
    # ##国际化
    # Babel(app)
    # ##moment
    # moment = Moment(app)
    # ##登录管理
    # login_manager.init_app(app)
    # ##调试工具
    # with app.app_context():
    #     if current_app.debug:
    #         DebugToolbarExtension(app)
    ##邮箱
    mail.init_app(app)
    ##注册蓝本
    regist_app(app)

    return app
