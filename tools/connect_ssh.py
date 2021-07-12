#!/usr/bin/env python
# encoding: utf-8
"""
@version: v1.0
@author: liubowen
@contact: 15178940382@163.com
@site: http://www.liubowen.icu/
@software: PyCharm
@file: connect_ssh.py
@time: 2021/4/22 15:38
"""
import paramiko
from paramiko.ssh_exception import NoValidConnectionsError, AuthenticationException, SSHException


class connect(object):
    def __init__(self, hostname, port, username, passwd):
        self.hostname = hostname
        self.port = port
        self.username = username
        self.passwd = passwd

    def do_conn(self):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        try:
            ssh.connect(hostname=self.hostname, port=self.port, username=self.username, password=self.passwd,
                        timeout=10)
            print("正在连接%s......." % (self.hostname))
        except NoValidConnectionsError as e:
            print("连接失败!", e.errors)
            ssh.close()
        except AuthenticationException as e:
            print("密码错误！", e.args)
        else:
            return ssh

    def do_cmd(self, command):
        con = self.do_conn()
        stdin, stout, stderr = con.exec_command(command)
        result = stout.read().decode('utf-8')
        return result

    def do_close(self):
        self.do_conn().close()


if __name__ == '__main__':
    # ssh = paramiko.SSHClient()
    # ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    # ssh.connect(hostname='172.16.10.168', username='root', password='123456')
    # stdin, stdout, stderr = ssh.exec_command('/bin/df -Th')
    # result = stdout.read().decode('utf-8')
    # print(result)
    # ssh.close()
    con = connect(hostname='172.16.10.168', port='22', username='root', passwd='123456')
    command = "ps"
    result = con.do_cmd(command)
    print(result)
    con.do_close()
