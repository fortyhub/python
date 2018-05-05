#!/usr/bin/env python
# -*- coding:utf-8 -*-

#登录程序接口，用户尝试3次之后将会锁定。

import os, sys, getpass

os.system('clear') #清屏

count = 0  #登录次数计数

while count < 3:
    username = input('username:')
    lock_file = open('LockList.txt', 'r+')
    lock_list = lock_file.readlines()

    for lock_line in lock_list:
        if username == lock_line.strip('\n'):   #使用strip方法去除换行，比较用户名
            print('用户 %s 已被锁定，请联系管理员...' %(username))
            sys.exit(1)

    with open('UserList.txt', 'r') as user_file:
        user_list = user_file.readlines()

    for user_line in user_list:   #逐行读取
        user,passwd = user_line.strip('\n').split(':')
        if user == username:
            n = 0
            while n < 3:
                password = getpass.getpass('password:')
                if passwd == password:
                    print('欢迎 %s 登录系统!' %(username))
                    sys.exit(0)
                else:
                    if n != 2:
                        print('密码错误，请重新输入，您还有 %d 次机会\n' %(2-n))
                n += 1
            else:
                lock_file.write(username + '\n')
                sys.exit('错误次数过多，用户名已被锁定...')

    else:
        if count != 2:
            print('用户名不存在，请重试，您还有 %d 次机会\n' %(2-count))
    count += 1

else:
    sys.exit('输入次数过多，程序已退出...')

lock_file.close()

