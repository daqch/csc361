from socket import *
import sys

s = socket(AF_INET, SOCK_STREAM)
try:
    host = sys.argv[1]
    port = int(sys.argv[2])
    request = '/' + sys.argv[3]
    s.connect((host,port))
except:
    print("usage : python client.py 'host' 'port' 'requested-file'")
    sys.exit()
print ("Requesting " + request + " " + "from " + host +  " " + "with port number " + str(port))
fragments = []
s.send("GET " + request + " " + 'HTTP/1.1\n\n')
print("Answer: ")
while True:
    chunk = s.recv(10000)
    if not chunk:
        break
    fragments.append(chunk)
message = "".join(fragments)
print(message)
s.close()