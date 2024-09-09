import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Pygame Window with Image')

# Load the image
image = pygame.image.load('My pfp photos - copy.jpg')  
# Set the background color
background_color = (255, 255, 255)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the background
    window.fill(background_color)

    # Draw the image
    window.blit(image, (0, 0))

    # Update the display
    pygame.display.flip()
