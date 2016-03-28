import socket
import sys

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_ip = raw_input('Enter the IP address of Damian\'s machine: ')

server_address = (server_ip, 10030)
message =  raw_input("Enter your message: ")

try:

    # Send data
    print 'sending "%s"' % message
    sent = sock.sendto(message, server_address)

    # Receive response
    print 'waiting to receive'
    data, server = sock.recvfrom(4096)
    print 'received "%s"' % data

finally:
    # print 'closing socket'
    sock.close()