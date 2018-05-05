本程序是一个3次登录程序  超过3次会锁定
知识点 strip、readline、getpass以及打开文件的2种方式
open('file','r+')
with open('file','r+') as user_file:
	user_list = user_file.readlines()
