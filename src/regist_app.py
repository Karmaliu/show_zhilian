from flask import url_for, render_template

from src.admin.views import admin_app
from src.zhilian.urls import zhilian_app


def regist_app(app):
    app.register_blueprint(zhilian_app, url_prefix='/jobs')

    app.register_blueprint(admin_app, url_prefix='/admin')

    @app.route("/", methods=["GET"])
    def index():
        urls = [
            url_for("admin_app.index"),
            url_for("zhilian_app.company"),
            url_for("zhilian_app.jobs"),
            url_for("zhilian_app.relation")
        ]
        return render_template("index.html", urls=urls)
