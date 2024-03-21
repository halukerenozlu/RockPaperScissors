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
blue = (0, 0, 255)

# the loop
run = True
while run:
    computer_choice = random.choice(game_list)

