#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-01 11:29:03
# @Author  : wangmengcn (eclipse_sv@163.com)
# @Site    : https://eclipsesv.com
from pymongo import MongoClient

# MONGO_CONFIG
MONGO_CONFIG = {
    'host': 'localhost',
    'port': 27017
}

mongo = MongoClient(**MONGO_CONFIG)
