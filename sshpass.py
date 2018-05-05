#!/usr/bin/env python
# -*- coding:utf-8 -*-

#根据预设的iplist与密码列表以ssh的方式循环尝试验证正确的密码

#python的sshv2 protocol协议实现，用于py调用各种ssh功能
import paramiko
#py内置多线程模块
import threading
#py调试器
#import pdb

iplist = []
passwd = ['123','123456','12345678','@@lingtouniao@@']
#打开欲检测的ip列表文件
f = open("./item_list.txt", "r")
#遍历行，去除换行符，将ip附加到列表iplist
for line in f:
    line = line.strip('\n')
    iplist.append(line)
print iplist
print len(iplist)
#关闭文件
f.close()

#定义函数，传入欲检测的ip，密码，要执行的command
def ssh(ip,passwd,cmd):
    #建立sshclient对象
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print "------thread going to try:------", ip, "------"
    for pwd_try in passwd:
        try:
            ssh.connect(ip,22,'root',pwd_try,timeout=4,allow_agent=False,look_for_keys=False)
            stdin,stdout,stderr = ssh.exec_command(cmd)
            print "\n"
            print stdout.readlines()
            print "IP is: ", ip, " passwd is:", pwd_try + " trying right"
            print "\n"
            break
        except:
            print ip, " ", pwd_try + 'trying wrong'
            continue
    ssh.close()

if __name__ == '__main__':
    cmd = 'hostname'
    threads = [len(iplist)]
    print "*** threading start ***"
    for ip in iplist:
        thread = threading.Thread(target=ssh,args=(ip,passwd,cmd))
        thread.start()
