import random

print("""\tWelcome to a game of Rock, Paper, Scissors! \n
        Please choose one of the following options: \n
        1. Rock
        2. Paper
        3. Scissors
        4. Exit\n""")

game = {1 : "Rock", 2 : "Paper", 3 : "Scissors", 4 : "Exit game"}

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

    if (user_move, computer_move) in [("Rock", "Scissors"), ("Scissors", "Paper"), ("Paper", "Rock")]:
        print(f"Player wins, {user_move} beats {computer_move}")
    elif user_move == computer_move:
        print("Draw!")
    else:
        print(f"Computer wins, {computer_move} beats {user_move}")



