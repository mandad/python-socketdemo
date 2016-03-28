import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_ip = raw_input('Enter the IP address of Damian\'s machine: ')

server_address = (server_ip, 10040)
print 'connecting to %s port %s' % server_address
sock.connect(server_address)
try:
    
    # Send data
    message = raw_input('Enter your message: ')
    print 'sending "%s"' % message
    sock.sendall(message)

    # Look for the response
    amount_received = 0
    amount_expected = len(message)
    
    while amount_received < amount_expected:
        data = sock.recv(30)
        amount_received += len(data)
        print 'received "%s"' % data

finally:
    # print >>sys.stderr, 'closing socket'
    sock.close()