import random
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Rock Paper Scissors")
clock = pygame.time.Clock()

# starting values
game_list = ['Rock', 'Paper', 'Scissors']
computer = c = 0
command = cmd = 0
print("Score: Computer" + str(c) + "Player" + str(cmd))

# colors
blue = (52, 70, 235)
yellow = (237, 230, 24)

# the game loop
run = True
while run:
    computer_choice = random.choice(game_list)
    command = input("Rock, Paper, Scissors or Quit: ")
    if command == computer_choice:
        print("let's go")
    elif command == 'Rock':
        if computer_choice == 'Scissors':
            print("Player won!")
            cmd = cmd + 1
        else:
            print("Computer won")
            c = c + 1
    elif command == 'Paper':
        if computer_choice == 'Rock':
            print("Player won!")
            cmd = cmd + 1
        else:
            print("Computer won")
            c = c + 1
    elif command == 'Scissors':
        if computer_choice == 'Paper':
            print("Player won!")
            cmd = cmd + 1
        else:
            print("Computer won")
            c = c + 1
    elif command == 'Quit':
        break
    else:
        print("Wrong command!")
    print("Player: " + command)
    print("Computer: " + computer_choice)
    print("--------------")
    print("Score: Computer: " + str(c) + "Player: " + str(cmd))
    print("--------------")