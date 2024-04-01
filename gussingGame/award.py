def display_winners_award():
    # Set up the window
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Winner's Award")
    
    # Load the award image
    award_image = pygame.image.load("award.png")  # Replace "winner_award.png" with the actual image file
    
    # Get the size of the image
    image_width, image_height = award_image.get_size()
    # Calculate the position to center the image
    x = (screen_width - image_width) // 2
    y = (screen_height - image_height) // 2

    # Main loop for displaying the image
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
        
     # Clear the screen
        screen.fill((255, 255, 255))  # Fill with white background color
        
        # Display the award image centered on the screen
        screen.blit(award_image, (x, y))
        
        pygame.display.update()
    
    pygame.quit()
