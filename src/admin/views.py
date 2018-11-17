from flask import jsonify

from src.admin import admin_app


@admin_app.before_app_request
def before_request():
    print("before request")


@admin_app.route('/', methods=["POST", "GET"])
def index():
    return jsonify({"page": admin_app.url_prefix, "code": 404})
