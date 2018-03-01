#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-01 11:28:30
# @Author  : wangmengcn (eclipse_sv@163.com)
# @Site    : https://eclipsesv.com
from werkzeug.security import generate_password_hash, check_password_hash

from db_module.mongo import mongo

USER_COLLECTION = mongo['jwt']['user']


class User(object):
    """User Model"""

    def __init__(self, username, password):
        super(User, self).__init__()
        self.username = username
        self.password = password

    def create_user(self):
        if USER_COLLECTION.find_one({'username': self.username}):
            return {
                'error_code': 1,
                'msg': 'username has been used!'
            }
        try:
            USER_COLLECTION.insert_one({
                'username': self.username,
                'password': generate_password_hash(self.password)
            })
        except Exception as e:
            print(str(e))
        else:
            return {
                'error_code': 0,
                'msg': 'user:{} created'.format(self.username)
            }

    def check_password(self):
        user_info = USER_COLLECTION.find_one({
            'username': self.username
        })
        if not user_info:
            return {
                'error_code': 1,
                'msg': 'user:{} does not exist'.format(self.username)
            }
        if not check_password_hash(user_info.get('password'), self.password):
            return {
                'error_code': 1,
                'msg': 'username or password does not match'
            }
        return {
            'error_code': 0,
            'msg': 'username and password matches'
        }
