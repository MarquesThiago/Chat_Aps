import socket, threading, time

SERVER = "172.18.64.1"
PORT = 5051
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
# client.settimeout(10.0)

def handle_messages():
    while True:
        msg = client.recv(100000).decode()
        splited_message = msg.split('=')
        print(f'{splited_message[1]}: {splited_message[2]}')


def send(message):
    client.send(message.encode(FORMAT))


def send_messages():
    message = input('Send a message: ')
    send(f'msg={message}')

def send_files():
    time.sleep(1)
    message = input('Send a file: ')
    send(f'file={message}')
    try:
        # rb, cause exception is a read error
        with open(message, 'w') as file:
            while True:
                data = client.recv(1000000).decode('utf-8')
                if not message:
                    break
                print('iniciando tranferência de arquivo')
                file.write(data)
            # file.close()

            print(f'{message} foi recebido')
    except Exception as e:
        print("An exception occurred", e)

def send_author():
    name = input('Write your nickname: ')
    send(f'name={name}')

def start_sending():
    send_author()
    send_messages()
    # send_files()

def start():
    thread1 = threading.Thread(target=handle_messages)
    thread2 = threading.Thread(target=start_sending)
    thread1.start()
    thread2.start()

start()