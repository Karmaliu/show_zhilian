from src.admin.views import admin_app
from src.zhilian.views import zhilian_app


def regist_app(app):
    app.register_blueprint(zhilian_app, url_prefix='/')

    app.register_blueprint(admin_app, url_prefix='/admin')

