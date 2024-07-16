from common import *

def handle_messages(sock):
    while True:
        data = sock.recv(1024)
        print(f"client message: {data.decode('utf-8')}")

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    messages_handler = threading.Thread(target=handle_messages, args=(client_socket,))
    messages_handler.start()

    while True:
        message = input("Enter your message: ").encode('utf-8')
        # Prefix each message with a 4-byte length (network byte order)
        message = struct.pack('>I', len(message)) + message
        client_socket.sendall(message)
        

if __name__ == "__main__":
    main()