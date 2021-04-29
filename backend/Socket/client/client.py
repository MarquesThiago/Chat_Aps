import socket
import threading
import time

# ter portas diferentes

host = '127.0.0.1'
port = 1000

try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
except Exception as inst:
    print(inst)

"""
def receive_connection_to_server():
    while True:
        try:
            # request for echo connection from server
            message = client.recv(1024).decode('utf-8')
        except Exception as inst:
            # Close Connection
            print(inst)
            client.close()
            break
            """


def send_message_to_server():
    run = True
    while run:
        time.sleep(1)
        print(f'digite a mensagem>>>')
        message = f'{input()}'

        if(message == f'{"enviar"}'):
            name_file = str(input('digite o nome do arquivo>>>'))
            client.send(name_file.encode())
            receive_file_thread = threading.Thread(target=receive_file, args=(name_file,))
            receive_file_thread.start()
        else:
            client.send(message.encode('utf-8'))


def receive_file(name_file):
    # le e monta o arquivo
    #
    try:
        with open(name_file, 'rb') as file:
            while True:
                data = client.recv(1000000)
                if not data:
                    break
                file.write(data)
        print(f'{name_file} recebido')
    except Exception as inst:
        print(inst)
    client.close()


# Starting Threads
#receive_thread = threading.Thread(target=receive_connection_to_server)
#receive_thread.start()

send_thread = threading.Thread(target=send_message_to_server)
send_thread.start()

