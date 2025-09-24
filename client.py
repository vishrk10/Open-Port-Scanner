import socket
HOST =  '192.168.56.1'
PORT = 9090

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.connect((HOST,PORT))
while True:
  server.recv()
  
