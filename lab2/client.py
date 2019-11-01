from socket import *
import sys
import time

s = socket(AF_INET,SOCK_DGRAM)

host = '10.0.0.1'
port = 9000


for i in range(1,11):
	t = time.time()
	msg = "ping " + str(i) + " " + str(time.ctime(t))
	try:  
		s.sendto(msg, (host,port))
		s.settimeout(1)
		d = s.recvfrom(1050)
		reply = d[0]
		elapsed = str(round(time.time() - t,5)) + " seconds"
		print (reply + "" + "\n" + "time elapsed: " + elapsed)
	except Exception:
		print(" REQUEST TIMED OUT")
		continue
