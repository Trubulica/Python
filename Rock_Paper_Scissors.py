import random

game = {1 : "Rock", 2 : "Paper", 3 : "Scissors", 4 : "Exit game"}
print("""\tWelcome to a game of Rock, Paper, Scissors! \n
        Please choose one of the following options: \n
        1. Rock
        2. Paper
        3. Scissors
        4. Exit\n""")

while True:

    computer_choice = random.randint(1,3)
    user_input = int(input("You choose: " ))

    computer_move = game.get(computer_choice)
    user_move = game.get(user_input)

    if user_input == 4:
        print("Game over!")
        break
    elif user_input >= 5:
        print("Please choose a number from 1 to 4!")

    if computer_choice == 1:
        if user_input == 1:
            print("Draw!")
        elif user_input == 2:
            print(f"Player wins,", user_move, "beats", computer_move)
        elif user_input == 3:
            print(f"Computer wins,", computer_move, "beats", user_move)

    if computer_choice == 2:
        if user_input == 2:
            print("Draw!")
        elif user_input == 3:
            print(f"Player wins,", user_move, "beats", computer_move)
        elif user_input == 1:
            print(f"Computer wins,", computer_move, "beats", user_move)

    if computer_choice == 3:
        if user_input == 3:
            print("Draw!")
        elif user_input == 1:
            print(f"Player wins,", user_move, "beats", computer_move)
        elif user_input == 2:
            print(f"Computer wins,", computer_move, "beats", user_move)



