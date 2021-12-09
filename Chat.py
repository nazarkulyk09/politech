# client.py
import socket
import threading
import cezar

nickname = input("Choose your nickname : ").strip()
while not nickname:
    nickname = input("Your nickname should not be empty : ").strip()
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.56.1"  # "127.0.1.1"
port = 4444
code = 1
my_socket.connect((host, port))


def thread_sending():
    while True:
        message_to_send = str(input(''))
        code = int(input('Enter 2 to encode your message') or 1 )

        if message_to_send:
            if code == 2:
                message_to_send = cezar.myencode(message_to_send)
                message_with_nickname = nickname + " : " + message_to_send
            else:
                message_with_nickname = nickname + " : " + message_to_send
            my_socket.send(message_with_nickname.encode())


def thread_receiving():
    while True:
        message = my_socket.recv(1024).decode()
        print(message)

thread_send = threading.Thread(target=thread_sending)
thread_receive = threading.Thread(target=thread_receiving)
thread_send.start()
thread_receive.start()