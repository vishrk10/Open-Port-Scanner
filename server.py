import socket 

HOST = '192.168.56.1'
PORT = 9090

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((HOST,PORT))

server.listen(5)
while True:
    print("[Server is up and running!]")
    comport,ip = server.accept()
    print(f"connection established with{ip}")
    break
while True:
  server.send('sample.jpg')
  break
    

    
