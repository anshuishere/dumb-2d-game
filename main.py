import pygame
import sys
from character import Character
from boy_character import BoyCharacter
from initial_background import InitialBackground
from allen_background import AllenBackground
from vit_background import VITBackground
from bangalore_background import BangaloreBackground
from love_background import LoveBackground
from usa_background import USABackground
from corbett_background import CorbettBackground
from celebration import Celebration
from money_animation import MoneyAnimation
from leaf_animation import LeafAnimation
from magnifying_glass_animation import MagnifyingGlassAnimation
from heart_burst_animation import HeartBurstAnimation
from button import Button
from target import Target
from hurdle import Hurdle
from stage import Stage

# Initialize Pygame
pygame.init()

# Game settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple 2D Game")

def reset_game():
    global player, current_state, show_message, first_target_collected, second_target_collected
    global third_target_collected, bangalore_targets_collected, money_animation, leaf_animation
    global magnifying_animation, heart_animation, love_bg, meeting_message_shown, game_ended
    player = Character(50, HEIGHT - 100)
    current_state = INITIAL_STATE
    show_message = False
    first_target_collected = False
    second_target_collected = False
    third_target_collected = False
    bangalore_targets_collected = [False, False]
    money_animation = MoneyAnimation(WIDTH, HEIGHT)
    leaf_animation = LeafAnimation(WIDTH, HEIGHT)
    magnifying_animation = MagnifyingGlassAnimation(WIDTH, HEIGHT)
    heart_animation = HeartBurstAnimation(WIDTH, HEIGHT)
    love_bg = LoveBackground(WIDTH, HEIGHT)
    celebration = Celebration(WIDTH, HEIGHT)
    meeting_message_shown = False
    game_ended = False

# Create game objects
player = Character(50, HEIGHT - 100)
boy = BoyCharacter(WIDTH - 100, HEIGHT - 100)
initial_background = InitialBackground(WIDTH, HEIGHT)
allen_background = AllenBackground(WIDTH, HEIGHT)
vit_background = VITBackground(WIDTH, HEIGHT)
bangalore_background = BangaloreBackground(WIDTH, HEIGHT)
love_background = LoveBackground(WIDTH, HEIGHT)
usa_background = USABackground(WIDTH, HEIGHT)
corbett_background = CorbettBackground(WIDTH, HEIGHT)
current_stage = Stage()

# Create animations
celebration = Celebration(WIDTH, HEIGHT)
money_animation = MoneyAnimation(WIDTH, HEIGHT)
leaf_animation = LeafAnimation(WIDTH, HEIGHT)
magnifying_animation = MagnifyingGlassAnimation(WIDTH, HEIGHT)
heart_animation = HeartBurstAnimation(WIDTH, HEIGHT)

# Create reset button
reset_button = Button(WIDTH - 100, 20, 80, 30, "Reset", 24)

# Create hurdles
hurdles = [
    Hurdle(300, HEIGHT - 60),
    Hurdle(500, HEIGHT - 60),
    Hurdle(700, HEIGHT - 60)
]

# Add hurdles to stage
for hurdle in hurdles:
    current_stage.add_hurdle(hurdle)

# Create targets
kota_target = Target(WIDTH - 100, HEIGHT - 200)
vellore_target = Target(WIDTH - 100, HEIGHT - 200)
vit_target = Target(WIDTH - 100, HEIGHT - 200)
bangalore_targets = [
    Target(200, HEIGHT - 200),
    Target(400, HEIGHT - 200),
    Target(600, HEIGHT - 200)
]

# Game states
INSTRUCTION_STATE = "instruction"
INITIAL_STATE = "initial"
ALLEN_STATE = "allen"
VIT_STATE = "vit"
BANGALORE_STATE = "bangalore"
LOVE_STATE = "love"
USA_STATE = "usa"
CORBETT_STATE = "corbett"
current_state = INSTRUCTION_STATE
first_target_collected = False
second_target_collected = False
third_target_collected = False
bangalore_targets_collected = [False, False]
show_message = False
message_start_time = 0
current_message = ""
meeting_message_shown = False
transition_complete = False
can_proceed_to_usa = False
game_ended = False
end_message_start = 0
end_message_duration = 5000  # Show message for 5 seconds

# Text settings
font = pygame.font.Font(None, 36)
kota_message = "2014. Ishani goes to kota"
vellore_message = "Ishani goes to Vellore"
vit_message = "Ishani graduates from VIT"
bangalore_messages = [
    "Ishani joins Visa in Bangalore",
    "Ishani goes to Shillong",
    "Ishani is searching for love"
]
meeting_message = "Ishani meets Ritvik"

# Physics settings
GRAVITY = 0.8
JUMP_FORCE = -18
player_velocity = 0
is_jumping = False

def draw_instructions(screen):
    # Create a semi-transparent background for instructions
    instruction_surface = pygame.Surface((WIDTH, HEIGHT))
    instruction_surface.fill((0, 0, 0))
    instruction_surface.set_alpha(180)
    screen.blit(instruction_surface, (0, 0))
    
    # Title
    title_font = pygame.font.Font(None, 64)
    title = title_font.render("Journey of Love", True, (255, 255, 255))
    title_rect = title.get_rect(center=(WIDTH//2, 100))
    screen.blit(title, title_rect)
    
    # Instructions
    font = pygame.font.Font(None, 36)
    instructions = [
        "Welcome to Ishani and Ritvik's Journey!",
        "",
        "Controls:",
        "← → : Move Ishani left/right",
        "SPACE: Jump",
        "",
        "Goal:",
        "Guide Ishani through different stages",
        "Meet Ritvik and travel together",
        "Reach the final wedding stage",
        "",
        "Press ENTER to begin the journey!"
    ]
    
    y_offset = 180
    for line in instructions:
        if line:  # Only render non-empty lines
            text = font.render(line, True, (255, 255, 255))
            text_rect = text.get_rect(center=(WIDTH//2, y_offset))
            screen.blit(text, text_rect)
        y_offset += 40

# Game loop
clock = pygame.time.Clock()
running = True

while running:
    current_time = pygame.time.get_ticks()
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if current_state == INSTRUCTION_STATE and event.key == pygame.K_RETURN:
                current_state = INITIAL_STATE  # Move to initial state after instructions
            elif event.key == pygame.K_SPACE and not is_jumping:
                player_velocity = JUMP_FORCE
                is_jumping = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if reset_button.is_clicked(event.pos):
                reset_game()

    # Handle movement
    if current_state in [USA_STATE, CORBETT_STATE]:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.x -= player.speed
            boy.x = player.x + 40  # Keep boy slightly to the right
        if keys[pygame.K_RIGHT]:
            player.x += player.speed
            boy.x = player.x + 40
            
        # Keep both characters within screen bounds
        if player.x < 0:
            player.x = 0
            boy.x = 40
        elif player.x > WIDTH - player.width - 40:
            if current_state == USA_STATE:
                current_state = CORBETT_STATE
                player.x = 50
                boy.x = player.x + 40
            else:
                player.x = WIDTH - player.width - 40
                boy.x = WIDTH - player.width
    else:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.x -= player.speed
        if keys[pygame.K_RIGHT]:
            player.x += player.speed

    # Apply gravity
    player_velocity += GRAVITY
    player.move(0, player_velocity)

    # Ground collision
    if player.y > HEIGHT - 100:  # Ground level
        player.y = HEIGHT - 100
        player_velocity = 0
        is_jumping = False

    # Keep player in bounds and handle background transition
    if player.x < 0:
        player.x = 0
    elif player.x > WIDTH - player.width:
        if current_state == INITIAL_STATE:
            if first_target_collected:
                current_state = ALLEN_STATE
                player.x = 0
            else:
                player.x = WIDTH - player.width
        elif current_state == ALLEN_STATE:
            if second_target_collected:
                current_state = VIT_STATE
                player.x = 0
            else:
                player.x = WIDTH - player.width
        elif current_state == VIT_STATE:
            if third_target_collected:
                current_state = BANGALORE_STATE
                player.x = 0
            else:
                player.x = WIDTH - player.width
        elif current_state == BANGALORE_STATE:
            if bangalore_targets_collected[0]:  # Only need first target
                current_state = LOVE_STATE
                player.x = 0
                love_background.is_colorful = False
            else:
                player.x = WIDTH - player.width
        else:
            player.x = WIDTH - player.width

    # Check target collisions
    if current_state == INITIAL_STATE:
        if kota_target.check_collision(player):
            show_message = True
            message_start_time = current_time
            current_message = kota_message
            first_target_collected = True
    elif current_state == ALLEN_STATE:
        if vellore_target.check_collision(player):
            show_message = True
            message_start_time = current_time
            current_message = vellore_message
            second_target_collected = True
    elif current_state == VIT_STATE:
        if vit_target.check_collision(player):
            show_message = True
            message_start_time = current_time
            current_message = vit_message
            third_target_collected = True
            celebration.start()
    elif current_state == BANGALORE_STATE:
        for i, target in enumerate(bangalore_targets):
            if target.check_collision(player):
                if i == 1:
                    show_message = True
                    message_start_time = current_time
                    current_message = bangalore_messages[i]
                    leaf_animation.start()
                elif i == 2:
                    show_message = True
                    message_start_time = current_time
                    current_message = bangalore_messages[i]
                    magnifying_animation.start()
                elif not bangalore_targets_collected[i]:
                    show_message = True
                    message_start_time = current_time
                    current_message = bangalore_messages[i]
                    bangalore_targets_collected[i] = True
                    if i == 0:
                        money_animation.start()
    elif current_state == LOVE_STATE:
        if boy.check_collision(player):
            if not meeting_message_shown:
                show_message = True
                message_start_time = current_time
                current_message = meeting_message
                meeting_message_shown = True
                love_background.start_transition(current_time)
                heart_animation.start(player.x + player.width//2, player.y - 20)
                player.is_happy = True
                boy.is_happy = True
            elif player.x > WIDTH - player.width - 50 and love_background.met_boy:
                transition_complete = True
            if transition_complete and player.x > WIDTH - player.width - 50:
                can_proceed_to_usa = True
            if can_proceed_to_usa:
                current_state = USA_STATE
                player.x = 50
                boy.x = player.x + 40
    elif current_state == CORBETT_STATE:
        corbett_background.draw(screen)
        boy.draw(screen)
        # Check if both characters reached the target
        if corbett_background.check_target(player.x, player.y, boy.x, boy.y):
            player.is_happy = True
            boy.is_happy = True
            if not game_ended:
                game_ended = True
                end_message_start = pygame.time.get_ticks()  # Get current time for message

    # Clear screen first
    screen.fill((0, 0, 0))
    
    # Draw current background
    if current_state == INSTRUCTION_STATE:
        draw_instructions(screen)
    elif current_state == INITIAL_STATE:
        initial_background.draw(screen)
        kota_target.draw(screen)
        current_stage.draw(screen)
    elif current_state == ALLEN_STATE:
        allen_background.draw(screen)
        vellore_target.draw(screen)
    elif current_state == VIT_STATE:
        vit_background.draw(screen)
        vit_target.draw(screen)
    elif current_state == BANGALORE_STATE:
        bangalore_background.draw(screen)
        for target in bangalore_targets:
            target.draw(screen)
    elif current_state == LOVE_STATE:
        love_background.draw(screen, current_time)
        boy.draw(screen)
    elif current_state == USA_STATE:
        usa_background.draw(screen)
        boy.draw(screen)
    elif current_state == CORBETT_STATE:
        corbett_background.draw(screen)
        boy.draw(screen)
    
    # Update and draw all animations
    if current_state != LOVE_STATE and current_state != USA_STATE and current_state != CORBETT_STATE:  # Don't show animations in love or USA states
        celebration.update()
        celebration.draw(screen)
        money_animation.update()
        money_animation.draw(screen)
        leaf_animation.update()
        leaf_animation.draw(screen)
        magnifying_animation.update()
        magnifying_animation.draw(screen)
    
    # Heart animation shows in love state
    heart_animation.update()
    heart_animation.draw(screen)
    
    # Draw game objects
    player.draw(screen)

    # Draw reset button
    reset_button.draw(screen)

    # Draw message if needed
    if show_message:
        if current_time - message_start_time < 3000:
            text = font.render(current_message, True, (255, 255, 255))
            text_rect = text.get_rect(center=(WIDTH//2, HEIGHT//4))
            
            # Add a semi-transparent background for better readability
            bg_rect = text_rect.inflate(20, 10)
            bg_surface = pygame.Surface(bg_rect.size, pygame.SRCALPHA)
            pygame.draw.rect(bg_surface, (0, 0, 0, 128), bg_surface.get_rect())
            screen.blit(bg_surface, bg_rect)
            screen.blit(text, text_rect)
        else:
            show_message = False

    # Draw end game message
    if game_ended:
        current_time = pygame.time.get_ticks()  # Get current time for comparison
        if current_time - end_message_start < end_message_duration:
            # Create flashing effect by alternating visibility
            if (current_time - end_message_start) % 1000 < 500:  # Flash every half second
                font = pygame.font.Font(None, 72)  # Larger font for final message
                text = font.render("Happily Ever After!", True, (255, 255, 255))
                text_rect = text.get_rect(center=(WIDTH//2, HEIGHT//2))
                
                # Add a semi-transparent background for better readability
                bg_rect = text_rect.inflate(40, 20)
                bg_surface = pygame.Surface(bg_rect.size, pygame.SRCALPHA)
                pygame.draw.rect(bg_surface, (0, 0, 0, 180), bg_surface.get_rect())
                screen.blit(bg_surface, bg_rect)
                screen.blit(text, text_rect)
        else:
            running = False  # End the game after showing the message

    # Update display
    pygame.display.flip()
    
    # Control game speed
    clock.tick(60)

pygame.quit()
