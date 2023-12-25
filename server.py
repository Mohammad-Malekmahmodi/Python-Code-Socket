import time
import sys
import socket

print("\nWelcome To Chat Room\n")
print("Initialisting . . . . \n")
time.sleep(1)

s = socket.socket()
host = socket.gethostname()
ip = socket.gethostbyname(host)
port = 1234
s.bind((host,port))
print(host,"(",ip,")\n")
name = input(str("Enter Your Name: "))

s.listen(1)
print("\nWaiting For Incoming Connections . . . \n")
conn , addr = s.accept()
print("Received Connection From ",addr[0],"(",addr[1], ")\n")

s_name = conn.recv(1024)
s_name = s_name.decode()
print(s_name, "Has Connected To The Chat Room\nEnter [e] To Exit Chat Room\n")
conn.send(name.encode())

while True:
    message = input(str("Me :"))
    if message == "[e]":
        message = "Left Chat Room!"
        conn.send(message.encode())
        print("\n")
        break
    conn.send(message.encode())
    message = conn.recv(1024)
    message = message.decode()
    print(s_name,":",message)


