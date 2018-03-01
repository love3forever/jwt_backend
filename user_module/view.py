#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-01 11:54:08
# @Author  : wangmengcn (eclipse_sv@163.com)
# @Site    : https://eclipsesv.com
from flask_restful import Resource, Api, abort, request
from flask.blueprints import Blueprint
from flask import make_response, jsonify
from flask_jwt_extended import (
    create_access_token, jwt_required, get_jwt_identity,
    jwt_refresh_token_required, create_refresh_token,
    fresh_jwt_required
)

from .model import User

bp_user = Blueprint('user_module', __name__, url_prefix='/api/v1/user')
api_user = Api(bp_user)


@api_user.resource('/register')
class UserRegister(Resource):
    """用户注册路由"""

    def post(self):
        if request.is_json:
            request_data = request.get_json()
            username = request_data.get('username')
            password = request_data.get('password')
            current_user = User(username, password)
            create_user_response = current_user.create_user()
            if create_user_response.get('error_code'):
                abort(400, message=create_user_response.get('msg'))
            return make_response(jsonify(create_user_response))
        else:
            abort(400, message='post data should be in json format')


@api_user.resource('/login')
class UserLogin(Resource):
    """用户登陆"""

    def post(self):
        if request.is_json:
            request_data = request.get_json()
            username = request_data.get('username')
            password = request_data.get('password')
            current_user = User(username, password)
            check_user_password_response = current_user.check_password()
            if check_user_password_response.get('error_code'):
                abort(400, message=check_user_password_response.get('msg'))
            login_response = {
                'access_token': create_access_token(identity=username, fresh=True)
            }
            return make_response(jsonify(login_response))
        else:
            abort(400, message='post data should be in json format')


@api_user.resource('/refresh_login')
class RefreshUserLogin(Resource):
    """用户登陆"""

    def post(self):
        if request.is_json:
            request_data = request.get_json()
            username = request_data.get('username')
            password = request_data.get('password')
            current_user = User(username, password)
            check_user_password_response = current_user.check_password()
            if check_user_password_response.get('error_code'):
                abort(400, message=check_user_password_response.get('msg'))
            login_response = {
                'access_token': create_refresh_token(identity=username)
            }
            return make_response(jsonify(login_response))
        else:
            abort(400, message='post data should be in json format')


@api_user.resource('/info')
class UserInfo(Resource):
    """受保护view"""

    @jwt_required
    def get(self):
        current_user = get_jwt_identity()
        return make_response(jsonify({
            'current_user': current_user
        }))


@api_user.resource('/refresh_info')
class RefreshUserInfo(Resource):
    """docstring for RefreshUserInfo"""

    @jwt_refresh_token_required
    def get(self):
        current_user = get_jwt_identity()
        refresh_access_token = create_access_token(current_user, fresh=False)
        return make_response(jsonify({
            'new_token': refresh_access_token
        }))


@api_user.resource('/fresh_info')
class FreshUserInfo(Resource):
    """docstring for RefreshUserInfo"""

    @fresh_jwt_required
    def get(self):
        current_user = get_jwt_identity()
        return make_response(jsonify({
            'current_user': current_user
        }))
