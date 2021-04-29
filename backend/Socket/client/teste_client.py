from socket import socket
from threading import Thread


def waiting(tcp, send, host='localhost', port=5000):
    tcp.connect((host,port))

    while send.loop():
        print('Conected in ', host,'.')
        send.con = tcp

    while send.loop():
        msg = tcp.recv(1024)
        if not msg: break
        print(str(msg,'utf-8'))

if __name__ == '__main__':
    print('Write the domain or IP address of the server(localhost): ')
    host = input()
    if host == '':
        host = '127.0.0.1'


    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    send = Send()

    process = Thread(target = waiting, args = (tcp, send, host))
    process.start()
    print('')

    msg = input()
    while True:
        send.put(msg)
        msg = input()
    process.join()
    tcp.close()
    exit()