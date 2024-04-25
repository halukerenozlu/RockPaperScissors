import random
import datetime

# Starting values
game_list = ['Rock', 'Paper', 'Scissors']
computer = c = 0
command = cmd = 0

# Initial state
time = datetime.date.today()
print(time)
print("Score: Computer: " + str(c) + " Player: " + str(cmd))

# The game loop
Run = True
while Run:
    # Check if either player has reached the winning score before starting a new round
    if c == 3:
        print("Computer Won, Game Over!!")
        break
    elif cmd == 3:
        print("Player Won, Game Over!!")
        break

    computer_choice = random.choice(game_list)
    command = input("Rock, Paper, Scissors or Quit: ")

    # Check if the player wants to quit
    if command.lower() == 'quit':
        break

    if command in game_list:
        print("Player: " + command)
        print("Computer: " + computer_choice)

        # Determine the winner of the round
        if command == computer_choice:
            print("It's a tie!")
        elif (command == 'Rock' and computer_choice == 'Scissors') or \
                (command == 'Paper' and computer_choice == 'Rock') or \
                (command == 'Scissors' and computer_choice == 'Paper'):
            print("Player won!")
            cmd += 1
        else:
            print("Computer won")
            c += 1

        # Print the current score
        print("--------------")
        print("Score: Computer: " + str(c) + " Player: " + str(cmd))
        print("--------------")
    else:
        print("Wrong command!")

print("Game Over!")
