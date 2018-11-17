from flask import jsonify, request

from src.admin import admin_app


def get_ip(request):
    remote_addr = request.remote_addr
    access_route = request.access_route
    return remote_addr, access_route


@admin_app.before_app_request
def before_request():
    remote_addr, _ = get_ip(request)
    print("request:{}".format(remote_addr))


@admin_app.route('/', methods=["POST", "GET"])
def index():
    return jsonify({"page": admin_app.url_prefix, "code": 404})
