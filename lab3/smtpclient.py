from socket import *

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = "142.104.197.65"

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect(("142.104.197.65", 25))


recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
	print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'helo diegoaquinochavez\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')
    
# Send MAIL FROM command and print server response.
mailFromCommand = 'mail from: diegoaquinochavez@uvic.ca\r\n'
clientSocket.send(mailFromCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send RCPT TO command and print server response. 
rcptToCommand = 'rcpt to : <diego_6525@hotmail.com>\r\n'
clientSocket.send(rcptToCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')


# Send DATA command and print server response. 
dataCommand = 'data\r\n'
clientSocket.send(dataCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)


# Message ends with a single period.
messageCommand = "this is a test from python\r\n"
clientSocket.send(messageCommand.encode())
endCommand = ".\r\n"
clientSocket.send(endCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')



# Send QUIT command and get server response.
quitCommand = 'quit\r\n'
clientSocket.send(quitCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '221':
    print('221 reply not received from server.')