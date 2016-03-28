import sys
from socket import *
s = socket(AF_INET, SOCK_DGRAM)
s.bind(('',0))
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

s.sendto('Test Broadcast!', ('<broadcast>', 10010))
