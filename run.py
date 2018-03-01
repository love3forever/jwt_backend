#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-01 14:08:33
# @Author  : wangmengcn (eclipse_sv@163.com)
# @Site    : https://eclipsesv.com

from create_app import create_app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
