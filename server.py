import socket
#host = '127.0.0.1'
#port = 8080

s = socket.socket()
s.bind(('', 7575))

s.listen(1)
c,addr = s.accept()
print("A client connected")

while True:
    data = c.recv(1024)
    if not data:
        break
    print("From client: "+str(data.decode()))

    data1 = input("Enter response: ")

    c.send(data1.encode())

c.close