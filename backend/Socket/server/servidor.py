import socket
import threading

client_list = []
def port_free(ports, host):
    for port in ports:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            server.bind((host, port))
            return port, host
        except:
            print("porta fechada")
        finally:
            server.close()

def server(host, port):


    def connect_server(port,host):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((host, port))
        server.listen()
        print('servidor conectado')
        return server
    connect_server(port, host)


    def receive_client_request():
        while True:
            # Accept Connection
            address = (host, port)
            client, address = server.accept()
            print("Connected with")
        return client

    def submit_mensagem(mensagem):
        for client in client_list:
            client.send(mensagem)


    def receive_client_message(client):
        while True:
            try:
                message = client.recv(1024)
                thread = threading.Thread(target=submit_mensagem, args=(message,))
                thread.start()
            except Exception as e:
                # remove disconnected client
                print(e)
                index = client_list.index(client)
                client_list.remove(client)
                client.close()
                break
        return message

    def submit_file(client):
        name_file = client.recv(1024).decode()
        try:
            with open(name_file, 'rb') as file:
                for data in file.readlines():
                    client.send(data)
        except Exception as e:
            print("An exception occurred", e)


    def execute_func_server(client):

        receive_and_listener_thread = threading.Thread(target=receive_client_request)
        receive_and_listener_thread.start()


        receive_client_message_thread = threading.Thread(target=receive_client_message)
        receive_client_message_thread.start()


        submit_file_thread = threading.Thread(target=submit_file, args=(client,))
        submit_file_thread.start()

    execute_func_server_thread = threading.Thread(target=execute_func_server)
    execute_func_server_thread.start()



