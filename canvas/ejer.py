import pygame

pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Move Text with Mouse")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Set the font and text for the message
font = pygame.font.Font(None, 36)
text = font.render("Rodrigo Silva", True, BLACK)

# Get the size of the text surface
text_rect = text.get_rect()

# Set the initial position of the text
text_rect.centerx = screen.get_rect().centerx
text_rect.centery = screen.get_rect().centery

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # Check if the mouse button is pressed down
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Move the text to the mouse position
            text_rect.centerx, text_rect.centery = event.pos

    # --- Game logic should go here

    # --- Drawing code should go here

    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)

    # Draw the text surface onto the screen
    screen.blit(text, text_rect)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()