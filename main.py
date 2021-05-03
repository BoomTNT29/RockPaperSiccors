import random

def main():
    singeOrMulitplayer = input("Do you want to play with computer or with a real person(comp / person): ")
    if singeOrMulitplayer == "comp":
        comp()
    # elif singeOrMulitplayer == "person":
    #     global client
    #     import client
        # multiplayer()
    else:
        print("You choose the wrong option! \n try again!")
        main()

def comp():
    rockOrPaperOrSiccors = input("What do u choose (R, P ,S): ")
    RpcOfComputer = random.choice(["R", "P", "S"])

    print("You choose:", rockOrPaperOrSiccors)
    print("The computer choose:", RpcOfComputer)

    if rockOrPaperOrSiccors == RpcOfComputer:
        print("Draw!")
    elif rockOrPaperOrSiccors == "R" and RpcOfComputer == "P" or rockOrPaperOrSiccors == "S" and RpcOfComputer == "R" or RpcOfComputer == "S" and rockOrPaperOrSiccors == "P": #computer wins in this case
        print("Syke! You lose!")
    else: # layer wins here
        print("O0f, tryhard, congrats you have won!")

def multiplayer():
    print("Waiting for a player!")
    client.main()

for x in range(0, 10):
    main()