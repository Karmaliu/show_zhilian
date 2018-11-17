from flask import jsonify, url_for

from src.admin.views import admin_app
from src.zhilian import zhilian_app


def regist_app(app):
    app.register_blueprint(zhilian_app, url_prefix='/zhilian')

    app.register_blueprint(admin_app, url_prefix='/admin')

    @app.route("/", methods=["GET"])
    def index():
        urls = [
            url_for("admin_app.index"),
            url_for("zhilian_app.index")
        ]
        return jsonify({"urls": urls})
