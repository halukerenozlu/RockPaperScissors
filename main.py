import random

game_list = ['Rock', 'Paper', 'Scissors']
computer = c = 0
command = cmd = 0
print("Score: Computer" + str(c) + "Player" + str(cmd))
# the loop
run = True
while run:
    computer_choice = random.choice(game_list)
