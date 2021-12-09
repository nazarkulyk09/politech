# server.py
import socket
import threading
import pickle
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
PORT = 7777
ADDRESS = "0.0.0.0"
broadcast_list = []
my_socket.bind((ADDRESS, PORT))


def accept_loop():
    while True:
        my_socket.listen()
        client, client_address = my_socket.accept()
        broadcast_list.append(client)
        start_listenning_thread(client)


def start_listenning_thread(client):
    client_thread = threading.Thread(
        target=listen_thread,
        args=(client,)  # the list of argument for the function
    )
    client_thread.start()


def listen_thread(client):
    while True:
        message = pickle.loads(client.recv(1024))
        if message:
            print(message)
            broadcast(message)
        else:
            print(client)
            return


def broadcast(message):
    for client in broadcast_list:
        try:
            client.send(pickle.dumps(message))
        except:
            broadcast_list.remove(client)
            print(f"Client removed : {client}")


accept_loop()