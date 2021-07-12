#!/usr/bin/env python
# encoding: utf-8
"""
@version: v1.0
@author: liubowen
@contact: 15178940382@163.com
@site: http://www.liubowen.icu/
@software: PyCharm
@file: test.py
@time: 2021/4/21 17:09
"""
from remote_operation import SshRemoteHost

if __name__ == '__main__':
    str = input("请输入：")

    host_info = SshRemoteHost(hostname='172.16.10.168', port='22', user='root',
                              passwd='123456',
                              cmd=str)

    result = host_info.do_cmd()

    print(result)
