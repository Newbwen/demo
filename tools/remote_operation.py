#!/usr/bin/env python
# encoding: utf-8
"""
@version: v1.0
@author: liubowen
@contact: 15178940382@163.com
@site: http://www.liubowen.icu/
@software: PyCharm
@file: remote_operation.py
@time: 2021/4/21 16:22
"""
import paramiko
import os
from paramiko.ssh_exception import NoValidConnectionsError, AuthenticationException, SSHException


class SshRemoteHost(object):
    def __init__(self, hostname, port, username, passwd):
        self.hostname = hostname
        self.port = port
        self.username = username
        self.passwd = passwd

    def run(self):
        cmd_str = self.cmd.split()[0]
        print(cmd_str)
        if hasattr(self, 'do_' + cmd_str):
            getattr(self, 'do_' + cmd_str)()
        else:
            print("目前不支持该功能！")

    def do_cmd(self, cmd):
        client = paramiko.SSHClient()

        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            client.connect(hostname=self.hostname, port=self.port, username=self.username, password=self.passwd)
            print("正在连接%s......." % (self.hostname))
        except NoValidConnectionsError as e:
            print("连接失败")
        except AuthenticationException as e:
            print("密码错误")
        else:
            # 4. 执行操作
            cmd = ''.join(cmd.split()[1:])  ##将输入的后面的取出，作为
            stdin, stdout, stderr = client.exec_command(cmd)

            # 5.获取命令执行的结果
            result = stdout.read().decode('utf-8')
            print(result)
        finally:
            # 6.关闭连接
            client.close()

    def do_put(self):
        ###put /tmp/passwd  ###将本地的/tmp/passwd上传到远端/tmp/passwd
        print('正在上传...')
        try:
            # 获取Transport实例
            tran = paramiko.Transport(self.hostname, int(self.port))  ##由于端口为整型，而我们用split方法得到的是str
            # 连接SSH服务端
            tran.connect(username=self.username, password=self.passwd)
        except SSHException as e:
            print('连接失败')
        else:
            # 获取SFTP实例
            sftp = paramiko.SFTPClient.from_transport(tran)
            newCmd = self.cmd.split()[1:]
            if len(newCmd) == 2:

                # 设置上传的本地/远程文件路径
                localpath = newCmd[0]
                remotepath = newCmd[1]
                # 执行上传动作
                sftp.put(localpath, remotepath)
                print('%s文件上传到%s主机的%s文件成功' % (localpath, self.hostname, remotepath))
            else:
                print('上传文件信息错误')

                tran.close()

    def do_get(self):

        print('正在下载...')
        try:
            # 获取Transport实例
            tran = paramiko.Transport(self.hostname, int(self.port))  ##由于端口为整形，而我们用split方法得到的是str
            # 连接SSH服务端
            tran.connect(username=self.username, password=self.passwd)
        except SSHException as e:
            print('连接失败')
        else:
            # 获取SFTP实例
            sftp = paramiko.SFTPClient.from_transport(tran)
            newCmd = self.cmd.split()[1:]
            if len(newCmd) == 2:

                # 设置下载的本地/远程文件路径
                localpath = newCmd[1]
                remotepath = newCmd[0]
                # 执行上传动作
                sftp.get(remotepath, localpath)
                print('%s主机的%s文件下载到%s文件成功' % (self.hostname, remotepath, localpath))
            else:
                print('上传文件信息错误')

                tran.close()


if __name__ == '__main__':
    # ssh = paramiko.SSHClient()
    # ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    # ssh.connect(hostname='172.16.10.168', username='root', password='123456')
    # stdin, stdout, stderr = ssh.exec_command('/bin/df -Th')
    # result = stdout.read().decode('utf-8')
    # print(result)
    # ssh.close()
    ssh = SshRemoteHost(hostname='172.16.10.168', port='22', username='root',
                        passwd='123456')
    cmd = "df -Th"
    result = ssh.do_cmd(cmd=cmd)

    print(result)
