# Load the 'correct' sound effect
correct_sound = pygame.mixer.Sound("./sounds/correct.wav")

# Load the 'incorrect' sound effect
incorrect_sound = pygame.mixer.Sound("./sounds/incorrect.wav")

# Load the background music
background_music = pygame.mixer.Sound("./sounds/background_music.wav")

# Function to play the correct guess sound
# This function plays the 'correct' sound effect when the player guesses the correct number.

def play_correct_sound():
    correct_sound.play()

# Function to play the incorrect guess sound
# This function plays the 'incorrect' sound effect when the player's guess is incorrect.

def play_incorrect_sound():
    incorrect_sound.play()
