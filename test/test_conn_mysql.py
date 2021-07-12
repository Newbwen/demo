#!/usr/bin/env python
# encoding: utf-8
"""
@author: liubowen
@contact: 15178940382@163.com
@site: http://www.liubowen.icu/
@file: test_conn_mysql.py
@time: 2021/7/12 10:04
"""
from tools.connect_mysql import DBConnect

if __name__ == '__main__':
    conn = DBConnect(host='172.16.10.1', port=3306, db='test', user='root', passwd='pwd', charset='utf8')
    conn.execute('select * from test')
    print(conn)
    for i in conn:
        print(i)

