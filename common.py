import socket
import select
import threading
import multiprocessing
import itertools
import struct

host = '127.0.0.1'
port = 12345
buff_size = 1024

def send_message(sock, message: str):
    message = message.encode()
    message = struct.pack('>I', len(message)) + message
    sock.sendall(message)


def recv_message(sock)->str:
    # Read message length and unpack it into an integer
    raw_len = sock.recv(4)
    msg_len = struct.unpack('>I', raw_len)[0]
    data = bytearray()
    while len(data) < msg_len:
        temp_data = sock.recv(buff_size)
        if temp_data:
            data.extend(temp_data)
    message = data.decode()
    return message
