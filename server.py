from common import *


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    readers = [server_socket]

    while True:
        read_sockets, write_sockets, error_sockets = select.select(readers, [], [])
        for s in read_sockets:
            if s is server_socket:
                client_socket, client_address = server_socket.accept()
                print(f"Accepted connection from {client_address}")
                readers.append(client_socket)
            else:
                data = s.recv(1024)
                print('len', len(data))
                if data:
                    message = data.decode('utf-8')
                    print(f"server received message: {message}")
                    for client_socket in readers[1:]:
                        client_socket.send(message.encode())
                else:
                    #todo
                    pass

if __name__ == "__main__":
    main()  