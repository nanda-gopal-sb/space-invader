import pygame
pygame.init() # Initialize the game

screen = pygame.display.set_mode((800, 600)) # Create a screen with a size of 800x600 pixels
running = True
pygame.display.set_caption("Space Invaders") # Set the title of the game window# Game loop



player1 = pygame.image.load("space_shooter/spaceship.png")
playerX = 370
playerY = 480

def player():
    screen.blit(player1, (playerX, playerY))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0, 0, 0)) # Fill the screen with black color
    player()
    pygame.display.update() # Update the screen