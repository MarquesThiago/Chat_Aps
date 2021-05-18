import socket, threading, time

SERVER_IP = socket.gethostbyname(socket.gethostname())
print(socket.gethostbyname(socket.gethostname()))
PORT = 5051
ADDR = (SERVER_IP, PORT)
FORMAT = 'utf-8'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
# server.settimeout(10.0)

connections = []
messages = []

def send_message(connection):
    print('Sending messages...')
    for i in range(connection['last'], len(messages)):
        sending_message = 'msg=' + messages[i]
        connection['conn'].send(sending_message.encode())
        connection['last'] = i + 1
        time.sleep(0.2)

def send_message_all():
    global connections
    for connection in connections:
        send_message(connection)

def handle_clients(conn, addr):
    print(f'New connection: {addr}')
    global connections
    global messages
    name = False

    while(True):
        msg = conn.recv(1024).decode(FORMAT)
        if(msg):
            if(msg.startswith('name=')):
                splited_message = msg.split('=')
                name = splited_message[1]
                connection_map = {
                    'conn': conn,
                    'addr': addr,
                    'name': name,
                    'last': 0
                }
                connections.append(connection_map)
                send_message(connection_map)
            elif(msg.startswith('msg=')):
                splited_message = msg.split('=')
                message = f'{name}={splited_message[1]}'
                messages.append(message)
                send_message_all()
            elif(msg.startswith('file=')):
                splited_message = msg.split('=')
                name_file = splited_message[1]
                print(name_file)
                try:
                    with open(name_file, 'rb') as file:
                        for data in file.readlines():
                            conn.send(data)
                except Exception as e:
                    print("An exception occurred", e)


def start():
    print('Starting the server')
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_clients, args=(conn, addr))
        thread.start()

start()