#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-01 14:05:52
# @Author  : wangmengcn (eclipse_sv@163.com)
# @Site    : https://eclipsesv.com
from flask import Flask

from jwt_module.init_jwt import jwt, JWT_CONFIG
from user_module.view import bp_user


def create_app():
    # jwt config
    app = Flask(__name__)
    app.config.update(JWT_CONFIG)

    # blueprints
    app.register_blueprint(bp_user)

    jwt.init_app(app)

    return app
