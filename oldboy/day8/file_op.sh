#!/usr/bin/env python
#-*-coding:utf-8-*-

f=open('静夜思.txt','r')
#date=f.read()
#print(date)
#date=f.readline()
#print(date)

#for i in f.readlines():
#	print(i.strip())
#readlines会占用大量内存

number = 0
for i in f:  #for内部将f对象做成迭代器，用一行取一行。 
	number+=1
	if number == 3:
		i = ''.join([i.strip(), 'iiiii'])
	print(i.strip())

f.close()

#with 语句
with open('静夜思.txt','r') as f:
	f.read()
	f.readline()

print("您已退出with代码块")
