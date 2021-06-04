import socket

HOST = ''
PORT = 3000
dataSize = 4096

serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Create serverSock')

# Avoid WinError 10048(using port)
serverSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

serverSock.bind(('', PORT))
print('Bind serverSock')

serverSock.listen()
print('Listening...')

clientSock, addr = serverSock.accept()
print(f'Connection from {addr}')

while True:
    data = clientSock.recv(dataSize)

    print(f'Client> {data.decode()}')

    myData = str(input('Server> '))

    clientSock.sendall(myData.encode())

clientSock.close()
serverSock.close()