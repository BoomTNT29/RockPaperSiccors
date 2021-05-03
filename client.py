import time
import socket
import json
HEADER = 30
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "QUIT"
SERVER = "192.168.0.137"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def main():    
    found_player = client.recv(HEADER).decode(FORMAT)
    print("Connected to server!")
    print(found_player)
    if found_player == "True" or found_player == 'True':
        print("Found a player.")
    
    print("Starting game")
    start_game()

def start_game():
    RPC = input("What do u choose (R, P, S): ")
    if RPC == "R" or RPC == "P" or RPC == "S":
        RPC = RPC.encode(FORMAT)
        client.send(RPC)
    else:
        print("Choose something corect!")
        start_game()

    winOrLostOrDraw = client.recv(HEADER).decode(FORMAT)
    if winOrLostOrDraw == "draw":
        print("Ah man its a draw!")
    elif winOrLostOrDraw == "win":
        print("You win!")
    elif winOrLostOrDraw == "lost":
        print("you lose!")