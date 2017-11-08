#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ftplib
import os
import socket


HOST = raw_input("Please enter Connet server: ")
DIRN = '/'


def main():
	try:
		f = ftplib.FTP(HOST)
	except (socket.error, socket.gaierror) as e:
		print 'ERROR: cannot reach "%s"' % HOST
		return
	print '*** Conneted to host "%s"' % HOST

	try:
		f.login()
	except ftplib.error_perm:
		print 'ERROR: cannot login anonymously'
		f.quit()
		return
	print '*** Logined as "anonymous"'

	try:
		f.cwd(DIRN)
	except ftplib.error_perm:
		print 'ERROR: cannot CD to "%s"' % DIRN
		f.quit()
		return
	print '*** Changed to "%s" folder' % DIRN
	print f.dir()


if __name__ == '__main__':
	main()