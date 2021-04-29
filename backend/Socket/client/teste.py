import socket
import threading

def waiting(tcp, send, host='', port=5000):
    tcp.bind((host, port))
    tcp.listen(1)

    while True:
        con, client = tcp.accept()
        print('Client ', client, ' conected!')
        send.con = con

    while True:
        msg = con.recv(1024)
        if not msg: break
        print(str(msg,'utf-8'))


if __name__ == '__main__':

    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    send = Send()

    process = threading.Thread(target=waiting, args=(tcp, send))
    process.start()

    print('Starting the chat server...')
    print('Waiting for conections')

    msg = input()
    while True:
        send.put(msg)
        msg = input()

    process.join()
    tcp.close()
    exit()