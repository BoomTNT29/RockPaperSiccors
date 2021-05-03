import json
import socket
import threading
import random

HEADER = 30
PORT = 5050
SERVER = "192.168.0.137"
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "QUIT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def main():
    server.listen()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(f"[LISTENING] Sever is listening on {SERVER}")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    
    conn_1, addr_1 = server.accept()
    print(f"Player one with {addr_1} connected.")

    conn_2, addr_2 = server.accept()
    print(f"Player two with {addr_2} connected.")

    msg = "True"
    msg = msg.encode(FORMAT)

    print("Sending confirmation")
    conn_1.send(msg)
    conn_2.send(msg)

    start_game(conn_1, conn_2)

def start_game(conn_1, conn_2):
    RpcForPlayerOne = conn_1.recv(HEADER).decode(FORMAT)
    RpcForPlayerTwo = conn_2.recv(HEADER).decode(FORMAT)

    if RpcForPlayerOne == RpcForPlayerTwo:
        conn_1.send(("draw").encode(FORMAT))
        conn_2.send(("draw").encode(FORMAT))
    elif RpcForPlayerOne == "R" and RpcForPlayerTwo == "P" or RpcForPlayerOne == "S" and RpcForPlayerTwo == "R" or RpcForPlayerTwo == "S" and RpcForPlayerOne == "P": #Player two wins in this case
        conn_1.send(("lost").encode(FORMAT))
        conn_2.send(("win").encode(FORMAT))
    else: #player one wins here
        conn_2.send(("lost").encode(FORMAT))
        conn_1.send(("win").encode(FORMAT))

for x in range(0, 10):
    main()
