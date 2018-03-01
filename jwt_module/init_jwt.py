#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-01 10:44:27
# @Author  : wangmengcn (eclipse_sv@163.com)
# @Site    : https://eclipsesv.com
from datetime import timedelta
from flask_jwt_extended import JWTManager
from flask import jsonify

# JWT_CONFIG
JWT_CONFIG = {
    'JWT_SECRET_KEY': 'she',
    'JWT_ACCESS_TOKEN_EXPIRES': timedelta(days=1),
    'JWT_REFRESH_TOKEN_EXPIRES': timedelta(days=25),
    'JWT_HEADER_TYPE': 'JWT'
}

# JWT CALLBACKS


jwt = JWTManager()


@jwt.expired_token_loader
def expored_token_loader_callback():
    return jsonify({
        'http_code': 401,
        'msg': 'The token has expired'
    })
