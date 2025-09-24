import socket 

ipaddr = '103.138.60.225'

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
for port in range(1,100):
   try:
    s .connect((ipaddr,port))
    print(f"the {port} port is open")
   except:
    print(f"the {port} is closed")  

   