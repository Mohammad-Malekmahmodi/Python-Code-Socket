import time
import sys
import socket

print("\nWelcome To Chat Room\n")
print("Initialisting . . . . \n")
time.sleep(1)

s = socket.socket()
host = socket.gethostname()
ip = socket.gethostbyname(host)
print(host,"(",ip,")\n")
host = input(str("Enter Server Address: "))
name = input(str("Enter Your Name: "))
port = 1234
print("\nTrying To ",host,"(",port, ")\n")
time.sleep(1)
s.connect((host,port))
print("Connected. . .\n")


s.send(name.encode())
s_name = s.recv(1024)
s_name = s_name.decode()
print(s_name, "Has Joined The Chat Room\nEnter [e] To Exit Chat Room\n")


while True:
    message = s.recv(1024)
    message = message.decode()
    print(s_name,":",message)
    message = input(str("Me : "))
    if message == "[e]":
        message = "Left Chat Room!"
        s.send(message.encode())
        print("\n")
        break
    s.send(message.encode())

