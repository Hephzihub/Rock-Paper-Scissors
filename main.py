import random

gameName = "Welcome to The R-ROCK, P-PAPER and S-SCISSORS Game"
instrc = "This game takes in one input and input can be R which stands Rock, P which stands Paper, S which stands Scissors. It will be played against a computer \n<-!!GAME RULES-!!> \n=>Rock beats Scissors \n=>Paper beats Rock \n=>Scissors beats Paper"
errMSG = "!!!!You entered the wrong choice!!!"

print(gameName)
print(instrc)

possibleChoice = ["R", "P", "S"]

def playGame():

    # Take player input
    playerChoice = input("Enter one of these letters ('R' -> Rock, 'P' -> Paper, 'S' -> Scissors)>>> ").upper()

    #ensures payer input is among the listed choice
    while playerChoice not in possibleChoice:
        print(errMSG)
        playerChoice = input("Enter one of these letters ('R' -> Rock, 'P' -> Paper, 'S' -> Scissors)>>> ").upper()

    if playerChoice == "R":
        playerChoice = "ROCK"
    elif playerChoice == "P":
        playerChoice = "PAPER"
    elif playerChoice == "S":
        playerChoice = "SCISSORS"


    # Selects CPU choice
    cpuChoice = random.choice(possibleChoice)

    if cpuChoice == "R":
        cpuChoice = "ROCK"
    elif cpuChoice == "P":
        cpuChoice = "PAPER"
    elif cpuChoice == "S":
        cpuChoice = "SCISSORS"

    print(f"Player ({playerChoice}): CPU ({cpuChoice})")

    # Checks who wins
    if playerChoice == cpuChoice:
        print("You drew")
        return playGame()

    elif playerChoice == "ROCK":
        if cpuChoice == "SCISSORS":
            print("Rock beats Scissors! Player WINS!!!")
        else:
            print("Paper beats Rock! CPU WIN!!!")

    elif playerChoice == "PAPER":
        if cpuChoice == "ROCK":
            print("Paper beats Rock! Player WINS!!!")
        else:
            print("Scissors beats Paper! CPU WINS!!!")

    elif playerChoice == "SCISSORS":
        if cpuChoice == "PAPER":
            print("Scissors beats Paper! Player WINS!!!")
        else:
            print("Rock beats Scissors! CPU WINS!!!")

playGame()
