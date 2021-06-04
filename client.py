import socket

HOST = '10.94.20.128'
PORT = 3000
dataSize = 4096

clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Create clientSock')

clientSock.connect((HOST, PORT))
print('Your connected!')

while True:
    myData = str(input('Client> '))
    clientSock.sendall(myData.encode())

    data = clientSock.recv(dataSize)
    print(f'Server> {data.decode()}')

clientSock.close()