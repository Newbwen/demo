#!/usr/bin/env python
# encoding: utf-8
"""
@author: liubowen
@contact: 15178940382@163.com
@site: http://www.liubowen.icu/
@file: devops_fabric.py
@time: 2021/7/12 14:34
"""
from fabric.connection import Connection


def deploy():
    conn = Connection("root@172.16.10.12", connect_kwargs={"password": "123456"})
    conn.run("ls")

    with conn.cd('/home'):
        conn.run("mkdir test")
        conn.put('1.txt', '/home/test')


if __name__ == '__main__':
    deploy()
