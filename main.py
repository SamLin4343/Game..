import pygame
from pygame import mixer
from Controller import Character

mixer.init()
pygame.init()

# Game Size
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("SAM Lin CS110 Final Project")

# Set framerate
clock = pygame.time.Clock()
FPS = 60

# Define colours
RED = (216, 36, 41)
BLUE = (173, 216, 230)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

# Define game variables
intro_count = 3
last_count_update = pygame.time.get_ticks()
score = [0, 0]  # player scores. [P1, P2]
round_over = False
ROUND_OVER_COOLDOWN = 2000

# Define fighter variables
WARRIOR_SIZE = 162
WARRIOR_SCALE = 4
WARRIOR_OFFSET = [72, 56]
WARRIOR_DATA = [WARRIOR_SIZE, WARRIOR_SCALE, WARRIOR_OFFSET]

WIZARD_SIZE = 250
WIZARD_SCALE = 3
WIZARD_OFFSET = [112, 107]
WIZARD_DATA = [WIZARD_SIZE, WIZARD_SCALE, WIZARD_OFFSET]

# Load music and sounds
pygame.mixer.music.load("assets/Sound Effects/music.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1, 0.0, 5000)
sword_fx = pygame.mixer.Sound("assets/Sound Effects/sword.wav")
sword_fx.set_volume(0.5)
magic_fx = pygame.mixer.Sound("assets/Sound Effects/magic.wav")
magic_fx.set_volume(0.75)

# Load background images
bg_images = [
    pygame.image.load("assets/Screen Images/BG1.png").convert_alpha(),
    pygame.image.load("assets/Screen Images/BG2.png").convert_alpha(),
    pygame.image.load("assets/Screen Images/BG3.png").convert_alpha()
]
current_bg_index = 0

# Load spritesheets
warrior_sheet = pygame.image.load("assets/Martial Hero (P1)/Sprites/warrior.png").convert_alpha()
wizard_sheet = pygame.image.load("assets/Evil Wizard (P2)/Sprites/wizard.png").convert_alpha()

# Load victory image
victory_img = pygame.image.load("assets/Screen Images/End.png").convert_alpha()

#load volume node
volume_wheel_img = pygame.image.load("assets/Screen Images/Mini sword .png").convert_alpha()
volume_wheel_rect = volume_wheel_img.get_rect()

# Define number of steps in each animation
WARRIOR_ANIMATION_STEPS = [10, 8, 1, 7, 7, 3, 7]
WIZARD_ANIMATION_STEPS = [8, 8, 1, 8, 8, 3, 7]

# Define font
count_font = pygame.font.Font("assets/Font/Iceberg-Regular.ttf", 80)
score_font = pygame.font.Font("assets/Font/Iceberg-Regular.ttf", 30)
menu_font = pygame.font.Font(None, 36)

# Initialize current_bg_index outside the loop
current_bg_index = 0

# Function for drawing text
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

# Function for drawing background
def draw_bg():
    scaled_bg = pygame.transform.scale(bg_images[current_bg_index], (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0, 0))

# Function for drawing fighter health bars
def draw_health_bar(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, WHITE, (x - 2, y - 2, 404, 34))
    pygame.draw.rect(screen, RED, (x, y, 400, 30))
    pygame.draw.rect(screen, YELLOW, (x, y, 400 * ratio, 30))

# Function to display start menu
def start_menu():
    global current_bg_index  # Move the global declaration here
    menu = True
    volume_slider_pos = SCREEN_WIDTH // 2
    menu_bg = pygame.image.load("assets/Screen Images/GUI_BG.jpg").convert_alpha()  # Load menu background image
    start_menu_img = pygame.image.load("assets/Screen Images/Start Menu.png").convert_alpha()  # Load start menu image
    start_menu_rect = start_menu_img.get_rect(topleft=(200, 200))  # Define start menu position

    # Load button images
    start_button_img = pygame.image.load("assets/Screen Images/start.png").convert_alpha()
    quit_button_img = pygame.image.load("assets/Screen Images/exist.png").convert_alpha()

    # Define button positions
    start_button_rect = start_button_img.get_rect(topleft=(200, 540))
    quit_button_rect = quit_button_img.get_rect(topleft=(475, 540))

    while menu:
        screen.fill((0, 0, 0))
        screen.blit(menu_bg, (0, 0))  # Draw menu background image

        # Draw start menu
        screen.blit(start_menu_img, start_menu_rect)

        # Draw volume slider
        pygame.draw.line(screen, WHITE, (200, 400), (720, 400), 5)
        volume_slider_pos = max(200, min(720, volume_slider_pos))

        # Draw volume wheel image
        volume_wheel_rect.centerx = volume_slider_pos
        volume_wheel_rect.centery = 400
        screen.blit(volume_wheel_img, volume_wheel_rect)

        # Draw buttons
        screen.blit(start_button_img, start_button_rect)
        screen.blit(quit_button_img, quit_button_rect)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                # Check if the mouse clicks on the start button
                if start_button_rect.collidepoint(mouse_pos):
                    menu = False
                # Check if the mouse clicks on the quit button
                elif quit_button_rect.collidepoint(mouse_pos):
                    pygame.quit()
                    quit()
            if event.type == pygame.MOUSEMOTION:
                if event.buttons[0] == 1:  # Check left mouse button is pressed
                    if 200 <= event.pos[0] <= 720:
                        volume_slider_pos = event.pos[0]
                        volume_level = (volume_slider_pos - 200) / 520
                        pygame.mixer.music.set_volume(volume_level)



# Create two instances of fighters
fighter_1 = Character(1, 200, 400, False, WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_STEPS, sword_fx)
fighter_2 = Character(2, 1500, 400, True, WIZARD_DATA, wizard_sheet, WIZARD_ANIMATION_STEPS, magic_fx)

# Start menu
start_menu()

# Game loop
run = True
while run:
    clock.tick(FPS)

    # Draw background
    draw_bg()

    # Show player stats
    draw_health_bar(fighter_1.health, 20, 20)
    draw_health_bar(fighter_2.health, 1500, 20)
    draw_text("P1: " + str(score[0]), score_font, BLUE, 20, 60)
    draw_text("P2: " + str(score[1]), score_font, RED, 1500, 60)

    # Update countdown
    if intro_count <= 0:
        # Move fighters
        fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2, round_over)
        fighter_2.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_1, round_over)
    else:
        # Display count timer
        draw_text(str(intro_count), count_font, RED, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3)
        # Update count timer
        if (pygame.time.get_ticks() - last_count_update) >= 1000:
            intro_count -= 1
            last_count_update = pygame.time.get_ticks()

    # Update fighters
    fighter_1.update()
    fighter_2.update()

    # Draw fighters
    fighter_1.draw(screen)
    fighter_2.draw(screen)

    # Check for player defeat
    if round_over == False:
        if fighter_1.alive == False:
            score[1] += 1
            round_over = True
            round_over_time = pygame.time.get_ticks()
        elif fighter_2.alive == False:
            score[0] += 1
            round_over = True
            round_over_time = pygame.time.get_ticks()
    else:
        # Display victory image
        screen.blit(victory_img, (730, 125))
        if pygame.time.get_ticks() - round_over_time > ROUND_OVER_COOLDOWN:
            round_over = False
            intro_count = 3
            # Change background after each round
            current_bg_index = (current_bg_index + 1) % len(bg_images)
            fighter_1 = Character(1, 200, 310, False, WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_STEPS, sword_fx)
            fighter_2 = Character(2, 1500, 310, True, WIZARD_DATA, wizard_sheet, WIZARD_ANIMATION_STEPS, magic_fx)

    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Update display
    pygame.display.update()

# Exit pygame
pygame.quit()