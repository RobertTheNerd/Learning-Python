import random


def game():
    a = input("rock, paper, or scissor: ")
    b = random.choice(["rock", "paper", "scissor"])

    print(f"Your choice is {a} and the computer's choice is {b}")

    compare(a, b)


def compare(value1, value2):
    value1 = value1.lower().strip()
    if value1 == value2:
        print("TIE")
    elif value1 == 'rock':
        if value2 == 'paper':
            print("You lose")
        else:
            print("You win")
    elif value1 == 'paper':
        if value2 == 'scissor':
            print("You lose")
        else:
            print("You win")
    elif value1 == 'scissor':
        if value2 == 'rock':
            print("You lose")
        else:
            print("You win")
    else:
        print('Not a valid game')

    print()



while True:
    game()
