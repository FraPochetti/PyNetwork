#!/usr/bin/env python
# -*- coding: latin-1 -*-

import socket, sys
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = sys.argv.pop() if len(sys.argv)==3 else '127.0.0.1'
PORT = 1060

def recv_all(sock):
    data = '' 
    more = sock.recv(1)
    data += more
    while more != '$':
        more = sock.recv(1)
        data += more
    return data

if sys.argv[1:] == ['server']:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(5)
    print 'Listening at', s.getsockname()
    sc, sockname = s.accept()
    print 'We have accepted a connection from', sockname
    print 'Socket connects', sc.getsockname(), 'and', sc.getpeername()
    while True:
      client_message = recv_all(sc)
      client_message = client_message[0:-1]
      print 'CLIENT SAYS: ', client_message
      server_message = raw_input('ME: ')
      server_message += '$'
      sc.sendall(server_message)
     # sc.close
     # print 'Reply sent, socket closed'

elif sys.argv[1:] == ['client']:
    s.connect((HOST, PORT))
    print 'Client has been assigned socket name', s.getsockname()
    while True:
      client_message = raw_input('ME: ')
      client_message += '$'
      s.sendall(client_message)
      server_message = recv_all(s)
      server_message = server_message[0:-1]
      print 'SERVER SAYS: ', server_message
     # s.close()

else:
   print 'DECIDE WHETHER YOU WANNA BE A CLIENT OR A SERVER!!!'
              
